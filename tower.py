"""
Provides all functions to build the tower of a crane
"""

import logging
from enum import Enum
import numpy

nodes = []
bars = []

SEGMENT_WIDTH = 2000
SEGMENT_HEIGHT = 2000
TOTAL_LENGTH = 0
NODES_FLOAT = []


class Style(Enum):
    """
    Enum to define a style how the bars of the tower are placed.
    Can be PARALLEL, CROSS or ZIGZAG
    """
    CROSS = 1
    ZIGZAG = 2
    DIAGONAL = 3


def create(number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create a tower

    Args:
    :param number_of_segments: Define how many segments the tower should have
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Using the Style Enum
    """
    create_segments(number_of_segments, has_horizontal, is_hollow, style_of_face)


def create_segment_beams(i, number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create all beams of a single segment of the tower

    Args:
    :param number_of_segments: Define the number of segments the tower has
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Using the Style Enum
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

    Args:
    :param i: current number of segment
    :param style_of_face: define the style of diagonal beams of each face. Using the Style Enum
    """
    if style_of_face == Style.DIAGONAL:  # hier stand parallel aber es gibt keine entsprechende enum
        create_parallel_face_beams_LR(i)
    elif style_of_face == Style.CROSS:
        create_cross_face_beam(i)
    elif style_of_face == Style.ZIGZAG:
        create_zigzag_face_beams(i)


def create_zigzag_face_beams(i):
    """All sides of the segments the tower is made of have zigzag bars to the top"""
    if i % 2 == 0:
        # For even numbers create diagonal from left to right
        create_parallel_face_beams_LR(i)
    else:
        # For odd numbers create diagonal from right to left
        create_parallel_face_beams_RL(i)


def create_cross_face_beam(i):
    """All sides of the segments the tower have a cross of beams"""
    val_to_add = 4 * i
    # front face
    bars.append([0 + val_to_add, 5 + val_to_add])
    add_length(0 + val_to_add, 5 + val_to_add)
    bars.append([4 + val_to_add, 1 + val_to_add])
    add_length(4 + val_to_add, 1 + val_to_add)
    # right face
    bars.append([5 + val_to_add, 3 + val_to_add])
    add_length(5 + val_to_add, 3 + val_to_add)
    bars.append([1 + val_to_add, 7 + val_to_add])
    add_length(1 + val_to_add, 7 + val_to_add)
    # rear face
    bars.append([2 + val_to_add, 7 + val_to_add])
    add_length(2 + val_to_add, 7 + val_to_add)
    bars.append([6 + val_to_add, 3 + val_to_add])
    add_length(6 + val_to_add, 3 + val_to_add)
    # left face
    bars.append([6 + val_to_add, 0 + val_to_add])
    add_length(6 + val_to_add, 0 + val_to_add)
    bars.append([2 + val_to_add, 4 + val_to_add])
    add_length(2 + val_to_add, 4 + val_to_add)
    # length of material used


def create_parallel_face_beams_RL(i):
    """Creates bottom right to top left diagonals"""
    val_to_add = 4 * i
    bars.append([4 + val_to_add, 1 + val_to_add])  # front face
    add_length(4 + val_to_add, 1 + val_to_add)
    bars.append([5 + val_to_add, 3 + val_to_add])  # right face
    add_length(5 + val_to_add, 3 + val_to_add)
    bars.append([7 + val_to_add, 2 + val_to_add])  # rear face
    add_length(7 + val_to_add, 2 + val_to_add)
    bars.append([6 + val_to_add, 0 + val_to_add])  # left face
    add_length(6 + val_to_add, 0 + val_to_add)


def create_parallel_face_beams_LR(i):
    """Creates bottom left to top right diagonals"""
    val_to_add = 4 * i
    bars.append([0 + val_to_add, 5 + val_to_add])  # front face
    add_length(0 + val_to_add, 5 + val_to_add)
    bars.append([5 + val_to_add, 3 + val_to_add])  # right face
    add_length(5 + val_to_add, 3 + val_to_add)
    bars.append([3 + val_to_add, 6 + val_to_add])  # rear face
    add_length(3 + val_to_add, 6 + val_to_add)
    bars.append([6 + val_to_add, 0 + val_to_add])  # left face
    add_length(6 + val_to_add, 0 + val_to_add)


def create_vertical_beams(i):
    """Create all vertical beams of a segment"""
    val_to_add = 4 * i
    bars.append([0 + val_to_add, 4 + val_to_add])  # front left vertical beam
    add_length(0 + val_to_add, 4 + val_to_add)
    bars.append([1 + val_to_add, 5 + val_to_add])  # front right vertical beam
    add_length(1 + val_to_add, 5 + val_to_add)
    bars.append([3 + val_to_add, 7 + val_to_add])  # rear left vertical beam
    add_length(3 + val_to_add, 7 + val_to_add)
    bars.append([2 + val_to_add, 6 + val_to_add])  # rear right vertical beam
    add_length(2 + val_to_add, 6 + val_to_add)


def create_horizontal_beams(i):
    """Create all horizontal beams of a segment"""
    val_to_add = 4 * i
    bars.append([0 + val_to_add, 1 + val_to_add])  # front horizontal beam
    add_length(0 + val_to_add, 1 + val_to_add)
    bars.append([1 + val_to_add, 3 + val_to_add])  # right horizontal beam
    add_length(1 + val_to_add, 3 + val_to_add)
    bars.append([3 + val_to_add, 2 + val_to_add])  # rear horizontal beam
    add_length(3 + val_to_add, 2 + val_to_add)
    bars.append([2 + val_to_add, 0 + val_to_add])  # left horizontal beam
    add_length(2 + val_to_add, 0 + val_to_add)


def create_segments(number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create all the different segment the tower is made of

    Args:
    :param number_of_segments: Define how many segments the tower should have
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Using the Style Enum
    """
    logging.debug("Initialize segment nodes")
    for i in range(number_of_segments + 1):
        logging.debug("Create nodes for segment: %s", i)
        create_segment_nodes(i)
    
    global NODES_FLOAT
    NODES_FLOAT = numpy.array(nodes).astype(float)

    logging.debug("Initialize segment beams")
    for i in range(number_of_segments + 1):
        logging.debug("Create beams for segment: %s", i)
        create_segment_beams(i, number_of_segments, has_horizontal, is_hollow, style_of_face)


def create_segment_nodes(i):
    """Create all nodes so the bars of a segment can connect to them"""
    nodes.append([0, 0, SEGMENT_HEIGHT * i])
    nodes.append([0, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])


def get_nodes():
    """Return the nodes of tower as numpy array of type float64"""
    return numpy.array(nodes).astype(float)


def get_nodes_raw():
    """Return nodes from internal array"""
    return nodes


def get_bars():
    """Return the bars of tower as numpy array"""
    return numpy.array(bars)


def get_bars_raw():
    """Return the bars of tower from internal array"""
    return bars


def add_length(start_node, end_node):
    """
    Calculates distance between 2 given points and adds it to a running length

    Args:
    :param start_node: start node of the beam
    :param end_node: end node of the beam
    """
    global TOTAL_LENGTH
    TOTAL_LENGTH += numpy.linalg.norm(NODES_FLOAT[end_node] - NODES_FLOAT[start_node])


def get_length():
    """Returns total length of material used in tower"""
    return TOTAL_LENGTH
