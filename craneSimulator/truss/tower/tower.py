"""
Provides all functions to build the tower of a crane
"""

import logging
from enum import Enum
import numpy as np


class Comps:
    """Component arrays for the tower"""
    nodes = []
    beams = []


class Style(Enum):
    """
    Enum to define a style how the beams of the tower are placed.
    Can be PARALLEL, CROSS or ZIGZAG
    """
    NONE = 0
    CROSS = 1
    ZIGZAG = 2
    DIAGONAL = 3


class Dims:
    """Class that contains all dimensions of the tower for global control"""
    SEGMENT_WIDTH = 0
    SEGMENT_HEIGHT = 0
    SEGMENTS = 0
    TOTAL_LENGTH = 0
    SUPPORT_TYPE = Style.NONE
    LONGEST_BEAM = 0


def create(has_horizontal, is_hollow):
    """
    Create a tower

    Args:
    :param has_horizontal: (Boolean) Should there be a horizontal between each segment
    :param is_hollow: (Boolean) Should the tower be empty or have beams in side
    """

    create_segments(has_horizontal, is_hollow)


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
        append_beam(0 + 4 * i, 2 + 4 * i)
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
        create_zigzag_face_beams(val_to_add)


def create_zigzag_face_beams(val_to_add):
    """All sides of the segments the tower is made of have zigzag beams to the top"""
    if (val_to_add / 4) % 2 == 0:
        # For even numbers create diagonal from left to right
        create_parallel_face_beams_LR(val_to_add)
    else:
        # For odd numbers create diagonal from right to left
        create_parallel_face_beams_RL(val_to_add)


def create_cross_face_beam(val_to_add):
    """All sides of the segments the tower have a cross of beams"""
    # front face
    append_beam(0 + val_to_add, 5 + val_to_add)
    append_beam(4 + val_to_add, 1 + val_to_add)
    # right face
    append_beam(5 + val_to_add, 3 + val_to_add)
    append_beam(1 + val_to_add, 7 + val_to_add)
    # rear face
    append_beam(2 + val_to_add, 7 + val_to_add)
    append_beam(6 + val_to_add, 3 + val_to_add)
    # left face
    append_beam(6 + val_to_add, 0 + val_to_add)
    append_beam(2 + val_to_add, 4 + val_to_add)
    # length of material used


def create_parallel_face_beams_RL(val_to_add):
    """Creates bottom right to top left diagonals"""
    append_beam(4 + val_to_add, 1 + val_to_add)  # front face
    append_beam(1 + val_to_add, 7 + val_to_add)  # right face
    append_beam(7 + val_to_add, 2 + val_to_add)  # rear face
    append_beam(2 + val_to_add, 4 + val_to_add)  # left face


def create_parallel_face_beams_LR(val_to_add):
    """Creates bottom left to top right diagonals"""
    append_beam(0 + val_to_add, 5 + val_to_add)  # front face
    append_beam(5 + val_to_add, 3 + val_to_add)  # right face
    append_beam(3 + val_to_add, 6 + val_to_add)  # rear face
    append_beam(6 + val_to_add, 0 + val_to_add)  # left face


def create_vertical_beams(val_to_add):
    """Create all vertical beams of a segment"""
    append_beam(0 + val_to_add, 4 + val_to_add)  # front left vertical beam
    append_beam(1 + val_to_add, 5 + val_to_add)  # front right vertical beam
    append_beam(3 + val_to_add, 7 + val_to_add)  # rear left vertical beam
    append_beam(2 + val_to_add, 6 + val_to_add)  # rear right vertical beam


def create_horizontal_beams(val_to_add):
    """Create all horizontal beams of a segment"""
    append_beam(0 + val_to_add, 1 + val_to_add)  # front horizontal beam
    append_beam(1 + val_to_add, 3 + val_to_add)  # right horizontal beam
    append_beam(3 + val_to_add, 2 + val_to_add)  # rear horizontal beam
    append_beam(2 + val_to_add, 0 + val_to_add)  # left horizontal beam
    if val_to_add != 0:
        append_beam(0 + val_to_add, 3 + val_to_add)


def create_segments(has_horizontal, is_hollow):
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
        create_segment_beams(i, Dims.SEGMENTS, has_horizontal, is_hollow, Dims.SUPPORT_TYPE)


def create_segment_nodes(elevation):
    """Create all nodes so the beams of a segment can connect to them"""
    Comps.nodes.append([0, 0, elevation])
    Comps.nodes.append([0, Dims.SEGMENT_WIDTH, elevation])
    Comps.nodes.append([Dims.SEGMENT_WIDTH, 0, elevation])
    Comps.nodes.append([Dims.SEGMENT_WIDTH, Dims.SEGMENT_WIDTH, elevation])


def append_beam(start_node, end_node):
    """
    Creates a beam between 2 given points and adds the length to a running total
    
    Args:
    :param start_node: start node of the beam
    :param end_node: end node of the beam
    """
    Comps.beams.append([start_node, end_node])
    start_float = np.array(Comps.nodes[start_node]).astype(float)
    end_float = np.array(Comps.nodes[end_node]).astype(float)
    length = np.linalg.norm(end_float - start_float)
    Dims.LONGEST_BEAM = max(length, Dims.LONGEST_BEAM)
    Dims.TOTAL_LENGTH += length


def get_nodes():
    """Return the nodes of tower as numpy array of type float64"""
    return np.array(Comps.nodes).astype(float)


def get_nodes_raw():
    """Return nodes from internal array"""
    return Comps.nodes


def get_beams():
    """Return the beams of tower as numpy array"""
    return np.array(Comps.beams)


def get_beams_raw():
    """Return the beams of tower from internal array"""
    return Comps.beams


def get_length():
    """Returns total length of material used in tower"""
    return Dims.TOTAL_LENGTH


def get_longest_beam():
    """Returns length of longest beam"""
    return Dims.LONGEST_BEAM


def get_height_width():
    """Gets the height and width of the tower"""
    return Dims.SEGMENT_HEIGHT * Dims.SEGMENTS, Dims.SEGMENT_WIDTH


def set_dims(height, width, segs, sup_style):
    """Sets dimensions of the tower to passed-through values"""
    Comps.nodes = []
    Comps.beams = []
    Dims.TOTAL_LENGTH = 0
    Dims.LONGEST_BEAM = 0

    Dims.SEGMENT_HEIGHT = height / segs
    Dims.SEGMENT_WIDTH = width
    Dims.SEGMENTS = segs
    if sup_style == 'None':
        Dims.SUPPORT_TYPE = Style.NONE
    elif sup_style == 'Cross':
        Dims.SUPPORT_TYPE = Style.CROSS
    elif sup_style == 'Zigzag':
        Dims.SUPPORT_TYPE = Style.ZIGZAG
    elif sup_style == 'Diagonal':
        Dims.SUPPORT_TYPE = Style.DIAGONAL


def default_dims():
    """Sets default parameters for the dimensions of the tower"""
    Dims.SEGMENT_HEIGHT = 1000
    Dims.SEGMENT_WIDTH = 1000
    Dims.SEGMENTS = 2
