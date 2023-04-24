"""
Provides all functions to build the jib of a crane
"""

import numpy

nodes = []
bars = []

SEGMENT_LENGTH = 2000
START_HEIGHT = 0
TOWER_WIDTH = 0
SEGMENTS = 0
IS_CONNECTED = False


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


def create_connected(tower_nodes, tower_bars, length, segments):
    """
    Creates jib attached to the tower as to have the entire crane in one block

    Args:
    :param tower_nodes: nodes which make up the tower (float[])
    :param tower_bars: bars which make up the tower (int[])
    :param length: length of the jib to be created  (float)
    :param segments: number of segments the jib should consist of (int)
    """
    global nodes
    nodes = tower_nodes
    global bars
    bars = tower_bars
    global SEGMENT_LENGTH
    SEGMENT_LENGTH = length / segments
    global SEGMENTS
    SEGMENTS = segments
    global IS_CONNECTED
    IS_CONNECTED = True

    create_segments()
    create_beams()


def create_segments():
    """
    Create the segments of a jib
    """
    for i in range(SEGMENTS + 1):
        if not (i == 0 and IS_CONNECTED):  # skips the first run-through if nodes already exist (i hope)
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, 0, START_HEIGHT])
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, TOWER_WIDTH, START_HEIGHT])
        if i < SEGMENTS:
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i + SEGMENT_LENGTH / 2, SEGMENT_LENGTH / 2,
                          START_HEIGHT + SEGMENT_LENGTH])


def create_beams():
    """
    Create all beams of a single segment
    """
    for i in range(SEGMENTS):
        create_horizontal_beams(len(bars) + i)
        create_diagonal_beams(len(bars) + i)


def create_horizontal_beams(i):
    """
    Create the horizontal beam of a segment
    :param i:
    """
    # connects all base nodes
    if i == 0 and not IS_CONNECTED:
        bars.append([0 + 3 * i, 1 + 3 * i])  # first horizontal (0-1)
    if i < SEGMENTS - 1:
        bars.append([2 + 3 * i, 5 + 3 * i])  # top connection
    bars.append([1 + 3 * i, 4 + 3 * i])
    bars.append([4 + 3 * i, 3 + 3 * i])
    bars.append([3 + 3 * i, 0 + 3 * i])
    bars.append([1 + 3 * i, 3 + 3 * i])  # diagonal beam


def create_diagonal_beams(i):
    """
    Create the diagonal beams of a segment, here the diagonal beams are the side of a pyramid
    :param i:
    """
    bars.append([0 + 3 * i, 2 + 3 * i])
    bars.append([1 + 3 * i, 2 + 3 * i])
    bars.append([4 + 3 * i, 2 + 3 * i])
    bars.append([3 + 3 * i, 2 + 3 * i])


def get_nodes():
    """
    Return the nodes of jib as numpy array of type float64
    """
    return numpy.array(nodes).astype(float)


def get_bars():
    """Return the bars of jib as numpy array"""
    return numpy.array(bars)
