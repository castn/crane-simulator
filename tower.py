import logging
from enum import Enum

import numpy

nodes = []
bars = []

SEGMENT_WIDTH = 2000
SEGMENT_HEIGHT = 2000


class Style(Enum):
    CROSS = 1
    ZICKZACK = 2
    PARALLEL = 3


def create(number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create a tower

    :param number_of_segments: Define how many segments the tower should have
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Can be PARALLEL (//), CROSS (X) or ZICKZACK (/\/)
    """
    create_segments(number_of_segments, has_horizontal, is_hollow, style_of_face)


def create_segment_beams(i, number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create all beams of a single segment of the tower

    :param number_of_segments: Define the number of segments the tower has
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Can be PARALLEL (//), CROSS (X) or ZICKZACK (/\/)
    """
    if has_horizontal:
        create_horizontal_beams(i)
    if not is_hollow:
        bars.append([0 + 4 * i, 2 + 4 * i])
    if i < number_of_segments:
        create_vertical_beams(i)
        create_diagonal_beams(i, style_of_face)


def create_diagonal_beams(i, style_of_face):
    """
    Create the diagonal beams on the faces of the tower.

    :param i: Current number of segment
    :param style_of_face: Define the style of diagonal beams of each face. Can be PARALLEL (//), CROSS (X) or ZICKZACK (/\/)
    """
    if style_of_face == Style.PARALLEL:
        create_parallel_face_beams_LR(i)
    elif style_of_face == Style.CROSS:
        create_cross_face_beam(i)
    elif style_of_face == Style.ZICKZACK:
        create_zickzack_face_beams(i)


def create_zickzack_face_beams(i):
    if i % 2 == 0:
        # For even numbers create diagonal from left to right
        create_parallel_face_beams_LR(i)
    else:
        # For odd numbers create diagonal from right to left
        create_parallel_face_beams_RL(i)


def create_cross_face_beam(i):
    # front face
    bars.append([0 + 4 * i, 5 + 4 * i])
    bars.append([4 + 4 * i, 1 + 4 * i])
    # right face
    bars.append([5 + 4 * i, 2 + 4 * i])
    bars.append([1 + 4 * i, 6 + 4 * i])
    # rear face
    bars.append([2 + 4 * i, 7 + 4 * i])
    bars.append([6 + 4 * i, 3 + 4 * i])
    # left face
    bars.append([7 + 4 * i, 0 + 4 * i])
    bars.append([3 + 4 * i, 4 + 4 * i])


def create_parallel_face_beams_RL(i):
    bars.append([4 + 4 * i, 1 + 4 * i])  # front face
    bars.append([1 + 4 * i, 6 + 4 * i])  # right face
    bars.append([6 + 4 * i, 3 + 4 * i])  # rear face
    bars.append([3 + 4 * i, 4 + 4 * i])  # left face


def create_parallel_face_beams_LR(i):
    bars.append([0 + 4 * i, 5 + 4 * i])  # front face
    bars.append([5 + 4 * i, 2 + 4 * i])  # right face
    bars.append([2 + 4 * i, 7 + 4 * i])  # rear face
    bars.append([7 + 4 * i, 0 + 4 * i])  # left face


def create_vertical_beams(i):
    bars.append([0 + 4 * i, 4 + 4 * i])  # front_left_vertical beam
    bars.append([1 + 4 * i, 5 + 4 * i])  # front_right_vertical beam
    bars.append([3 + 4 * i, 7 + 4 * i])  # rear_left_vertical beam
    bars.append([2 + 4 * i, 6 + 4 * i])  # rear_right_vertical beam


def create_horizontal_beams(i):
    bars.append([0 + 4 * i, 1 + 4 * i])  # front_horizontal beam
    bars.append([1 + 4 * i, 2 + 4 * i])  # right_horizontal beam
    bars.append([2 + 4 * i, 3 + 4 * i])  # rear_horizontal beam
    bars.append([3 + 4 * i, 0 + 4 * i])  # left_horizontal beam


def create_segments(number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create all the different segment the tower is made of.

    :param number_of_segments: Define how many segments the tower should have
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Can be PARALLEL (//), CROSS (X) or ZICKZACK (/\/)
    """
    logging.debug("Initialize segment nodes")
    for i in range(number_of_segments + 1):
        logging.debug(f"Create nodes for segment: {i}")
        create_segment_nodes(i)

    logging.debug("Initialize segment beams")
    for i in range(number_of_segments + 1):
        logging.debug(f"Create beams for segment: {i}")
        create_segment_beams(i, number_of_segments, has_horizontal, is_hollow, style_of_face)


def create_segment_nodes(i):
    nodes.append([0, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])
    nodes.append([0, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])


def get_nodes():
    return numpy.array(nodes).astype(float)


def get_bars():
    return numpy.array(bars)
