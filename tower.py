from enum import Enum

import numpy

nodes = []
bars = []

SEGMENT_WIDTH = 2000
SEGMENT_HEIGHT = 2000


class Style(Enum):
    CROSS = 1
    ZICKZACK = 2
    DIAGONAL = 3


def create(number_of_segments, has_horizontal, is_hollow, style_of_face):
    create_segments(number_of_segments)
    create_beams(number_of_segments, has_horizontal, is_hollow, style_of_face)


def create_beams(number_of_segments, has_horizontal, is_hollow, style_of_face):
    for i in range(number_of_segments + 1):
        print(f'Create segment: {i}')
        if has_horizontal:
            create_horizontal_beams(i)
        if not is_hollow:
            bars.append([0 + 4 * i, 2 + 4 * i])
        if i < number_of_segments:
            create_vertical_beams(i)
            create_diagonal_beams(i, style_of_face)


def create_diagonal_beams(i, style_of_face):
    if style_of_face == Style.DIAGONAL:
        bars.append([0 + 4 * i, 5 + 4 * i])  # front face
        bars.append([5 + 4 * i, 2 + 4 * i])  # right face
        bars.append([2 + 4 * i, 7 + 4 * i])  # rear face
        bars.append([7 + 4 * i, 0 + 4 * i])  # left face
    elif style_of_face == Style.CROSS:
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
    elif style_of_face == Style.ZICKZACK:
        if i % 2 == 0:
            # For even numbers create diagonal from left to right
            bars.append([0 + 4 * i, 5 + 4 * i])  # front face
            bars.append([5 + 4 * i, 2 + 4 * i])  # right face
            bars.append([2 + 4 * i, 7 + 4 * i])  # rear face
            bars.append([7 + 4 * i, 0 + 4 * i])  # left face
        else:
            # For odd numbers create diagonal from right to left
            bars.append([4 + 4 * i, 1 + 4 * i])  # front face
            bars.append([1 + 4 * i, 6 + 4 * i])  # right face
            bars.append([6 + 4 * i, 3 + 4 * i])  # rear face
            bars.append([3 + 4 * i, 4 + 4 * i])  # left face


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


def create_segments(number_of_segments):
    for i in range(number_of_segments + 1):
        create_segment(i)


def create_segment(i):
    nodes.append([0, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, 0, SEGMENT_HEIGHT * i])
    nodes.append([SEGMENT_WIDTH, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])
    nodes.append([0, SEGMENT_WIDTH, SEGMENT_HEIGHT * i])


def get_nodes():
    return numpy.array(nodes).astype(float)


def get_bars():
    return numpy.array(bars)
