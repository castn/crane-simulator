"""
Provides all functions to build the jib of a crane
"""

from enum import Enum
import numpy as np


class Comps:
    """Component arrays for the jib"""
    nodes = []
    beams = []


class Style(Enum):
    """
    Enum to define a style how the support of the jib is built
    Can be TRUSS or SET BACK TRUSS
    """
    NOT_CHOSEN = 0
    TRUSS = 1
    SET_BACK_TRUSS = 2


class Dims:
    """Class that contains all dimensions of the jib for global control"""
    SEGMENT_LENGTH = 0
    SEGMENTS = 0
    HEIGHT = 0
    SUPPORT_TYPE = Style.NOT_CHOSEN
    DROPDOWN = False
    BEND = False

    START_HEIGHT = 0
    TOWER_WIDTH = 0
    INIT_BEAM = 0
    END_BASE = 0

    IS_CONNECTED = False

    TOTAL_LENGTH = 0
    LONGEST_BEAM = 0


def create_sep(tower_height, tower_width, length, segments):
    """
    Creates jib separately from the tower but with the ability to connect to it

    Args:
    :param tower_height: height of the tower (float)
    :param tower_width: width of the tower (float)
    :param length: length of the jib to be created  (float)
    :param segments: number of segments the jib should consist of  (int)
    """
    Dims.START_HEIGHT = tower_height
    Dims.TOWER_WIDTH = tower_width
    Dims.SEGMENT_LENGTH = length / segments
    Dims.SEGMENTS = segments
    Dims.IS_CONNECTED = False

    create_segments()
    create_beams()


def create_connected(tower_nodes, tower_beams, tower_height, tower_width):
    """
    Creates jib attached to the tower as to have the entire crane in one block

    Args:
    :param tower_nodes: nodes which make up the tower (float[])
    :param tower_beams: beams which make up the tower (int[])
    :param length: length of the jib to be created  (float)
    :param segments: number of segments the jib should consist of (int)
    """
    Comps.nodes = tower_nodes
    Comps.beams = tower_beams

    Dims.START_HEIGHT = tower_height
    Dims.TOWER_WIDTH = tower_width
    Dims.IS_CONNECTED = True
    Dims.INIT_BEAM = max(np.asarray(Comps.beams).astype(int).max() - 1, 0)
    Dims.END_BASE = len(tower_nodes)

    create_segments()
    create_beams()


def create_segments():
    """Create the segments of a jib"""
    jib_length_m = Dims.SEGMENTS * Dims.SEGMENT_LENGTH / 1000
    for i in range(Dims.SEGMENTS + 1):
        len_in_m = Dims.TOWER_WIDTH / 1000 + Dims.SEGMENT_LENGTH / 1000 * i
        bend_grad = 0.01 * np.power(30, 1/jib_length_m * len_in_m) * 1000
        bot_height = Dims.START_HEIGHT + bend_grad if Dims.BEND else Dims.START_HEIGHT
        # skips the first run-through if nodes already exist
        if not (i == 0 and Dims.IS_CONNECTED):
            Comps.nodes.append([Dims.TOWER_WIDTH + Dims.SEGMENT_LENGTH * i,
                                0,
                                bot_height])
            Comps.nodes.append([Dims.TOWER_WIDTH + Dims.SEGMENT_LENGTH * i,
                                Dims.TOWER_WIDTH,
                                bot_height])
        if Dims.DROPDOWN:
            if i <= 3 * Dims.SEGMENTS / 7:
                top_height = Dims.HEIGHT
            elif i >= 5 * Dims.SEGMENTS / 7:
                top_height = 0.76 * Dims.HEIGHT
            else:
                count = i - 2 * Dims.SEGMENTS / 7
                top_height = Dims.HEIGHT - count * (0.24 * 7 * Dims.HEIGHT / (2 * jib_length_m))
                top_height = max(top_height, 0.76 * Dims.HEIGHT)
        else:
            top_height = Dims.HEIGHT
        # adds top nodes
        if i < Dims.SEGMENTS:
            Comps.nodes.append([Dims.TOWER_WIDTH + Dims.SEGMENT_LENGTH * i + Dims.SEGMENT_LENGTH / 2
                                if Dims.SUPPORT_TYPE == Style.TRUSS
                                else Dims.TOWER_WIDTH * 1.15 + Dims.SEGMENT_LENGTH * i,
                                Dims.SEGMENT_LENGTH / 2,
                                bot_height + top_height])


def create_beams():
    """Create all beams of a single segment"""
    for i in range(Dims.SEGMENTS):
        val_to_add = 3 * i + Dims.INIT_BEAM
        create_horizontal_beams(i, val_to_add)
        create_diagonal_beams(val_to_add)


def create_horizontal_beams(i, val_to_add):
    """Create the horizontal beams of a segment, here representing the bottom structure and top"""
    if i == 0 and not Dims.IS_CONNECTED:
        append_beam(0 + val_to_add, 1 + val_to_add)  # first horizontal (0-1)
    if i < Dims.SEGMENTS - 1:
        append_beam(2 + val_to_add, 5 + val_to_add)  # top connection
    append_beam(1 + val_to_add, 4 + val_to_add)
    append_beam(4 + val_to_add, 3 + val_to_add)
    append_beam(3 + val_to_add, 0 + val_to_add)
    append_beam(1 + val_to_add, 3 + val_to_add)     # bottom diagonal beam


def create_diagonal_beams(val_to_add):
    """Create the diagonal beams of a segment, here the diagonal beams are the side of a pyramid"""
    append_beam(0 + val_to_add, 2 + val_to_add)
    append_beam(1 + val_to_add, 2 + val_to_add)
    append_beam(4 + val_to_add, 2 + val_to_add)
    append_beam(3 + val_to_add, 2 + val_to_add)


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
    """Return the nodes of jib as numpy array of type float64"""
    return np.array(Comps.nodes).astype(float)


def get_nodes_raw():
    """Returns the nodes of the tower in original format"""
    return Comps.nodes


def get_beams():
    """Return the beams of jib as numpy array"""
    return np.array(Comps.beams)


def get_beams_raw():
    """Returns the beams of the tower in original format"""
    return Comps.beams


def get_length():
    """Returns total length of all beams"""
    return Dims.TOTAL_LENGTH


def get_longest_beam():
    """Returns length of longest beam"""
    return Dims.LONGEST_BEAM


def get_end_base():
    """Returns last node of base of jib"""
    return len(Comps.nodes) # len(Comps.nodes) if Dims.SUPPORT_TYPE == Style.TRUSS else (len(Comps.nodes) - 1)


def get_height():
    """Returns height of jib support structure"""
    return Dims.HEIGHT


def get_segments():
    """Returns nuber of segments"""
    return Dims.SEGMENTS


def get_support_type():
    """Returns support type of jib as an int"""
    return Dims.SUPPORT_TYPE.value


def set_dims(length, height, segs, sup_type, dropwdown, bend):
    """Sets dimensions of the jib to passed-through values"""
    Comps.nodes = []
    Comps.beams = []
    Dims.END_BASE = 0
    Dims.TOTAL_LENGTH = 0
    Dims.LONGEST_BEAM = 0

    Dims.SEGMENTS = segs
    Dims.SEGMENT_LENGTH = length / segs
    Dims.HEIGHT = height
    Dims.SUPPORT_TYPE = Style.TRUSS if sup_type == 'Truss' else Style.SET_BACK_TRUSS
    Dims.DROPDOWN = dropwdown
    Dims.BEND = bend


def default_dims():
    """Sets default parameters for the dimensions of the jib"""
    Dims.SEGMENTS = 2
    Dims.SEGMENT_LENGTH = 1000
    Dims.HEIGHT = 1000
