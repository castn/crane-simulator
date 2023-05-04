"""
Provides all functions to build the jib of a crane
"""

import numpy as np

nodes = []
beams = []

SEGMENT_LENGTH = 2000
START_HEIGHT = 0
TOWER_WIDTH = 0
SEGMENTS = 0
IS_CONNECTED = False
INIT_BAR = 0
TOTAL_LENGTH = 0


def create(tower_height, tower_width, length, segments):
    """
    Creates jib separately from the tower but with the ability to connect to it

    Args:
    :param tower_height: height of the tower (float)
    :param tower_width: width of the tower (float)
    :param length: length of the jib to be created  (float)
    :param segments: number of segments the jib should consist of  (int)
    """
    global START_HEIGHT
    START_HEIGHT = tower_height
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global SEGMENT_LENGTH
    SEGMENT_LENGTH = length / segments
    global SEGMENTS
    # SEGMENTS = int(length / SEGMENT_LENGTH)
    SEGMENTS = segments
    global IS_CONNECTED
    IS_CONNECTED = False

    create_segments()
    create_beams()


def create_connected(tower_nodes, tower_beams, tower_height, tower_width, length, segments):
    """
    Creates jib attached to the tower as to have the entire crane in one block

    Args:
    :param tower_nodes: nodes which make up the tower (float[])
    :param tower_beams: beams which make up the tower (int[])
    :param length: length of the jib to be created  (float)
    :param segments: number of segments the jib should consist of (int)
    """
    global nodes
    nodes = tower_nodes
    global beams
    beams = tower_beams
    global START_HEIGHT
    START_HEIGHT = tower_height #(np.asarray(nodes).astype(float))[len(nodes) - 1, 2]
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global SEGMENT_LENGTH
    SEGMENT_LENGTH = length / segments
    global SEGMENTS
    SEGMENTS = segments
    global IS_CONNECTED
    IS_CONNECTED = True
    global INIT_BAR
    INIT_BAR = max(np.asarray(beams).astype(int).max() - 1, 0) # wrapped in max just in case

    create_segments()
    create_beams()


def create_segments():
    """Create the segments of a jib"""
    for i in range(SEGMENTS + 1):
        if not (i == 0 and IS_CONNECTED):  # skips the first run-through if nodes already exist
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, 0, START_HEIGHT])
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, TOWER_WIDTH, START_HEIGHT])
        if i < SEGMENTS:
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i + SEGMENT_LENGTH / 2, SEGMENT_LENGTH / 2,
                          START_HEIGHT + (SEGMENT_LENGTH * 3/4)])


def create_beams():
    """Create all beams of a single segment"""
    for i in range(SEGMENTS):
        val_to_add = 3 * i + INIT_BAR
        create_horizontal_beams(i, val_to_add)
        create_diagonal_beams(val_to_add)


def create_horizontal_beams(i, val_to_add):
    """Create the horizontal beams of a segment"""
    if i == 0 and not IS_CONNECTED:
        append_beam(0 + val_to_add, 1 + val_to_add)  # first horizontal (0-1)
    if i < SEGMENTS - 1:
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
    return np.array(nodes).astype(float)


def get_nodes_raw():
    """Returns the nodes of the tower in original format"""
    return nodes


def get_beams():
    """Return the beams of jib as numpy array"""
    return np.array(beams)


def get_beams_raw():
    """Returns the beams of the tower in original format"""
    return beams


def append_beam(start_node, end_node):
    """
    Creates a beam between 2 given points and adds the length to a running total
    
    Args:
    :param start_node: start node of the beam
    :param end_node: end node of the beam
    """
    beams.append([start_node, end_node])
    global TOTAL_LENGTH
    start_float = np.array(nodes[start_node]).astype(float)
    end_float = np.array(nodes[end_node]).astype(float)
    TOTAL_LENGTH += np.linalg.norm(end_float - start_float)


def get_length():
    """Returns total length of all beams"""
    return TOTAL_LENGTH
