"""
Provides all functions to build the jib of a crane
"""

import numpy as np


class Comps:
    """Component arrays for the jib"""
    nodes = []
    beams = []


class Dims:
    """Class that contains all dimensions of the jib for global control"""
    SEGMENT_LENGTH = 0
    SEGMENTS = 0
    HEIGHT = 0

    START_HEIGHT = 0
    TOWER_WIDTH = 0
    INIT_BAR = 0

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
    Dims.INIT_BAR = max(np.asarray(Comps.beams).astype(
        int).max() - 1, 0)  # wrapped in max just in case

    create_segments()
    create_beams()


def create_segments():
    """Create the segments of a jib"""
    for i in range(Dims.SEGMENTS + 1):
        # skips the first run-through if nodes already exist
        if not (i == 0 and Dims.IS_CONNECTED):
            Comps.nodes.append([Dims.TOWER_WIDTH + Dims.SEGMENT_LENGTH * i,
                                0,
                                Dims.START_HEIGHT])
            Comps.nodes.append([Dims.TOWER_WIDTH + Dims.SEGMENT_LENGTH * i,
                                Dims.TOWER_WIDTH,
                                Dims.START_HEIGHT])
        if i < Dims.SEGMENTS:
            Comps.nodes.append([Dims.TOWER_WIDTH + Dims.SEGMENT_LENGTH * i + Dims.SEGMENT_LENGTH / 2,
                                Dims.SEGMENT_LENGTH / 2,
                                Dims.START_HEIGHT + Dims.HEIGHT])


def create_beams():
    """Create all beams of a single segment"""
    for i in range(Dims.SEGMENTS):
        val_to_add = 3 * i + Dims.INIT_BAR
        create_horizontal_beams(i, val_to_add)
        create_diagonal_beams(val_to_add)


def create_horizontal_beams(i, val_to_add):
    """Create the horizontal beams of a segment"""
    if i == 0 and not Dims.IS_CONNECTED:
        append_beam(0 + val_to_add, 1 + val_to_add)  # first horizontal (0-1)
    if i < Dims.SEGMENTS - 1:
        append_beam(2 + val_to_add, 5 + val_to_add)  # top connection
    append_beam(1 + val_to_add, 4 + val_to_add)
    append_beam(4 + val_to_add, 3 + val_to_add)
    append_beam(3 + val_to_add, 0 + val_to_add)
    append_beam(1 + val_to_add, 3 + val_to_add)  # diagonal beam


def create_diagonal_beams(val_to_add):
    """Create the diagonal beams of a segment, here the diagonal beams are the side of a pyramid"""
    append_beam(0 + val_to_add, 2 + val_to_add)
    append_beam(1 + val_to_add, 2 + val_to_add)
    append_beam(4 + val_to_add, 2 + val_to_add)
    append_beam(3 + val_to_add, 2 + val_to_add)


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


def get_length():
    """Returns total length of all beams"""
    return Dims.TOTAL_LENGTH


def get_longest_beam():
    """Returns length of longest beam"""
    return Dims.LONGEST_BEAM


def get_dims():
    """Prompts user to enter custom measurements for the jib in the console"""
    length = 0
    while length < 500 or length > 10000:  # 5000-10000
        length = float(input('Enter the length of the jib in mm: '))
    seg_length = 0
    segs = 0
    while seg_length < 500 or seg_length > 2000:  # 500-2000
        segs = int(input('Enter the how many segments you would like: '))
        seg_length = length / segs
    height = 0
    while height < 500 or height > 2000:
        height = float(input('Enter the height of the truss in mm: '))
    if np.sqrt(height ** 2 + (1/2 * np.sqrt(seg_length ** 2 + Dims.TOWER_WIDTH ** 2)) ** 2) > 2000:
        print(
            f'Warning! The diagonal elements will have a length of {np.sqrt(height ** 2 + (1/2 * np.sqrt(seg_length ** 2 + Dims.TOWER_WIDTH ** 2)) ** 2):.3f}mm which is greater than the 2000mm allowed!')
        print('Please adjust the measurements and reenter them.')
        get_dims()

    Dims.SEGMENTS = segs
    Dims.SEGMENT_LENGTH = seg_length
    Dims.HEIGHT = height


def set_dims(length, height, segs):
    """Sets dimensions of the jib to passed-through values"""
    Comps.nodes = []
    Comps.beams = []
    Dims.TOTAL_LENGTH = 0
    
    Dims.SEGMENTS = segs
    Dims.SEGMENT_LENGTH = length / segs
    Dims.HEIGHT = height


def default_dims():
    """Sets default parameters for the dimensions of the jib"""
    Dims.SEGMENTS = 2
    Dims.SEGMENT_LENGTH = 1000
    Dims.HEIGHT = 1000
