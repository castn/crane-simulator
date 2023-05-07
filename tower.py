"""
Provides all functions to build the tower of a crane
"""

import logging
from enum import Enum
import numpy as np

nodes = []
beams = []


class Dims:
    """Class that contains all dimensions of the tower for global control"""
    SEGMENT_WIDTH = 0
    SEGMENT_HEIGHT = 0
    SEGMENTS = 0
    TOTAL_LENGTH = 0


class Style(Enum):
    """
    Enum to define a style how the beams of the tower are placed.
    Can be PARALLEL, CROSS or ZIGZAG
    """
    CROSS = 1
    ZIGZAG = 2
    DIAGONAL = 3


def create(has_horizontal, is_hollow, style_of_face):
    """
    Create a tower

    Args:
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Using the Style Enum
    """

    create_segments(has_horizontal, is_hollow, style_of_face)


def create_segment_beams(i, number_of_segments, has_horizontal, is_hollow, style_of_face):
    """
    Create all beams of a single segment of the tower

    Args:
    :param number_of_segments: Define the number of segments the tower has
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Using the Style Enum
    """
    val_to_add = 4 * i
    if has_horizontal:
        create_horizontal_beams(val_to_add)
    if not is_hollow:
        append_bar(0 + 4 * i, 2 + 4 * i)
    if i < number_of_segments:
        create_vertical_beams(val_to_add)
        create_diagonal_beams(val_to_add, style_of_face)


def create_diagonal_beams(val_to_add, style_of_face):
    """
    Create the diagonal beams on the faces of the tower.

    Args:
    :param i: current number of segment
    :param style_of_face: define the style of diagonal beams of each face. Using the Style Enum
    """
    if style_of_face == Style.DIAGONAL:  # hier stand parallel aber es gibt keine entsprechende enum
        create_parallel_face_beams_LR(val_to_add)
    elif style_of_face == Style.CROSS:
        create_cross_face_beam(val_to_add)
    elif style_of_face == Style.ZIGZAG:
        create_zigzag_face_beams(i, val_to_add)


def create_zigzag_face_beams(i, val_to_add):
    """All sides of the segments the tower is made of have zigzag beams to the top"""
    if i % 2 == 0:
        # For even numbers create diagonal from left to right
        create_parallel_face_beams_LR(val_to_add)
    else:
        # For odd numbers create diagonal from right to left
        create_parallel_face_beams_RL(val_to_add)


def create_cross_face_beam(val_to_add):
    """All sides of the segments the tower have a cross of beams"""
    # front face
    append_bar(0 + val_to_add, 5 + val_to_add)
    append_bar(4 + val_to_add, 1 + val_to_add)
    # right face
    append_bar(5 + val_to_add, 3 + val_to_add)
    append_bar(1 + val_to_add, 7 + val_to_add)
    # rear face
    append_bar(2 + val_to_add, 7 + val_to_add)
    append_bar(6 + val_to_add, 3 + val_to_add)
    # left face
    append_bar(6 + val_to_add, 0 + val_to_add)
    append_bar(2 + val_to_add, 4 + val_to_add)
    # length of material used


def create_parallel_face_beams_RL(val_to_add):
    """Creates bottom right to top left diagonals"""
    append_bar(4 + val_to_add, 1 + val_to_add)  # front face
    append_bar(5 + val_to_add, 3 + val_to_add)  # right face
    append_bar(7 + val_to_add, 2 + val_to_add)  # rear face
    append_bar(6 + val_to_add, 0 + val_to_add)  # left face


def create_parallel_face_beams_LR(val_to_add):
    """Creates bottom left to top right diagonals"""
    append_bar(0 + val_to_add, 5 + val_to_add)  # front face
    append_bar(5 + val_to_add, 3 + val_to_add)  # right face
    append_bar(3 + val_to_add, 6 + val_to_add)  # rear face
    append_bar(6 + val_to_add, 0 + val_to_add)  # left face


def create_vertical_beams(val_to_add):
    """Create all vertical beams of a segment"""
    append_bar(0 + val_to_add, 4 + val_to_add)  # front left vertical beam
    append_bar(1 + val_to_add, 5 + val_to_add)  # front right vertical beam
    append_bar(3 + val_to_add, 7 + val_to_add)  # rear left vertical beam
    append_bar(2 + val_to_add, 6 + val_to_add)  # rear right vertical beam


def create_horizontal_beams(val_to_add):
    """Create all horizontal beams of a segment"""
    append_bar(0 + val_to_add, 1 + val_to_add)  # front horizontal beam
    append_bar(1 + val_to_add, 3 + val_to_add)  # right horizontal beam
    append_bar(3 + val_to_add, 2 + val_to_add)  # rear horizontal beam
    append_bar(2 + val_to_add, 0 + val_to_add)  # left horizontal beam


def create_segments(has_horizontal, is_hollow, style_of_face):
    """
    Create all the different segment the tower is made of

    Args:
    :param number_of_segments: Define how many segments the tower should have
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    :param style_of_face: Define the style of diagonal beams of each face. Using the Style Enum
    """
    logging.debug("Initialize segment nodes")
    for i in range(Dims.SEGMENTS + 1):
        logging.debug("Create nodes for segment: %s", i)
        elevation = Dims.SEGMENT_HEIGHT * i
        create_segment_nodes(elevation)


    logging.debug("Initialize segment beams")
    for i in range(Dims.SEGMENTS + 1):
        logging.debug("Create beams for segment: %s", i)
        create_segment_beams(i, Dims.SEGMENTS, has_horizontal, is_hollow, style_of_face)


def create_segment_nodes(elevation):
    """Create all nodes so the beams of a segment can connect to them"""
    nodes.append([0, 0, elevation])
    nodes.append([0, Dims.SEGMENT_WIDTH, elevation])
    nodes.append([Dims.SEGMENT_WIDTH, 0, elevation])
    nodes.append([Dims.SEGMENT_WIDTH, Dims.SEGMENT_WIDTH, elevation])


def get_nodes():
    """Return the nodes of tower as numpy array of type float64"""
    return np.array(nodes).astype(float)


def get_nodes_raw():
    """Return nodes from internal array"""
    return nodes


def get_beams():
    """Return the beams of tower as numpy array"""
    return np.array(beams)


def get_beams_raw():
    """Return the beams of tower from internal array"""
    return beams


def append_bar(start_node, end_node):
    """
    Creates a beam between 2 given points and adds the length to a running total
    
    Args:
    :param start_node: start node of the beam
    :param end_node: end node of the beam
    """
    beams.append([start_node, end_node])
    start_float = np.array(nodes[start_node]).astype(float)
    end_float = np.array(nodes[end_node]).astype(float)
    Dims.TOTAL_LENGTH += np.linalg.norm(end_float - start_float)


def get_length():
    """Returns total length of material used in tower"""
    return Dims.TOTAL_LENGTH


def get_dims():
    """Prompts to enter custom measurements for the tower"""
    height = 0
    while height < 500 or height > 10000: # 5000-10000
        height = float(input('Enter the height of the tower in mm: '))
    seg_height = 0
    segs = 0
    while seg_height < 500 or seg_height > 2000: # 500-2000
        segs = int(input('Enter the how many segments you would like: '))
        seg_height = height / segs
    width = 0
    while width < 500 or width > 2000: # 500-2000
        width = float(input('Enter the width of the crane in mm: '))
    if np.sqrt(seg_height ** 2 + width ** 2) > 2000:
        print(f'Warning! The diagonal elements will have a length of {np.sqrt(seg_height ** 2 + width ** 2):.3f}mm which is greater than the 2000mm allowed!')
        print('Please adjust the measurements and reenter them.')
        get_dims()

    Dims.SEGMENT_HEIGHT = seg_height
    Dims.SEGMENT_WIDTH = width
    Dims.SEGMENTS = segs


def default_dims():
    """Sets default parameters for the dimensions of the tower"""
    Dims.SEGMENT_HEIGHT = 1000
    Dims.SEGMENT_WIDTH = 1000
    Dims.SEGMENTS = 2


def get_height_width():
    """Gets the height and width of the tower"""
    return Dims.SEGMENT_HEIGHT * Dims.SEGMENTS, Dims.SEGMENT_WIDTH
