"""
Provides all functions to build the counterjib of a crane
"""

import numpy

nodes = []
beams = []

SEGMENT_LENGTH = 2000
START_HEIGHT = 0
TOWER_WIDTH = 0
SEGMENTS = 0
NODES_FLOAT = []
IS_CONNECTED = False
END_NODE_TOWER = 0
END_NODE_JIB = 2
TOTAL_LENGTH = 0


def create(tower_width, length):
    """
    Creates a counterjib separatley from the other components of the crane
    
    Args:
    :pram tower_width: width of the tower of the crane
    :param length: desired length of the counterjib
    """
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global SEGMENTS
    SEGMENTS = int(length / SEGMENT_LENGTH)
    
    create_segments()
    create_beams()


def create_connected(crane_nodes, crane_beams, tower_height, tower_width, tower_num_nodes, length):
    """
    Creates a counterjib with desired dimensions connected to the rest of the crane
    
    Args:
    :param crane_nodes: array of nodes used by the crane
    :param crane_beams: array of beams used by the crane
    :param tower_height: height of the tower of the crane
    :param tower_width: width of the tower of the crane
    :param tower_num_nodes: number of nodes used to construct the tower
    :param length: desired length of the counterjib
    """
    global nodes
    nodes = crane_nodes
    global beams
    beams = crane_beams
    global START_HEIGHT
    START_HEIGHT = tower_height
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global SEGMENTS
    SEGMENTS = int(length / SEGMENT_LENGTH)
    global IS_CONNECTED
    IS_CONNECTED = True
    global END_NODE_TOWER
    END_NODE_TOWER = tower_num_nodes - 4
    global END_NODE_JIB
    END_NODE_JIB = len(crane_nodes)
    
    create_segments()
    
    global NODES_FLOAT
    NODES_FLOAT = numpy.array(nodes).astype(float)
    
    create_beams()
    create_support()


def create_segments():
    """Creates all beams needed for the counterjib"""
    for i in range(SEGMENTS + 1):
        if not (i == 0 and IS_CONNECTED):  # skips the first run-through if nodes already exist
            nodes.append([- SEGMENT_LENGTH * i, 0, START_HEIGHT])
            nodes.append([- SEGMENT_LENGTH * i, TOWER_WIDTH, START_HEIGHT])


def create_beams():
    """Creates all beams needed for the counterjib"""
    start_node_cj = END_NODE_JIB #len(nodes)
    if not IS_CONNECTED:
        append_bar(0, 1)
    for i in range(SEGMENTS):
        val_to_add = 2 * (i - 1)
        create_frame_beams(i, start_node_cj, val_to_add)
        create_diag_beams(i, start_node_cj, val_to_add)
        

def create_frame_beams(i, start_node_cj, val_to_add):
    """Creates the outer frame of the counterjib"""
    if i == 0:
        append_bar(END_NODE_TOWER, start_node_cj)
        append_bar(END_NODE_TOWER + 1, start_node_cj + 1)
    else:
        append_bar(start_node_cj + val_to_add, start_node_cj + 2 + val_to_add)
        append_bar(start_node_cj + 1 + val_to_add, start_node_cj + 3 + val_to_add)
    append_bar(start_node_cj + val_to_add + 2, start_node_cj + 1 + val_to_add + 2)


def create_diag_beams(i, start_node_cj, val_to_add):
    """Creates the diagonal beams of the counterjib"""
    if i == 0:
        append_bar(END_NODE_TOWER, start_node_cj + 1)
        append_bar(END_NODE_TOWER + 1, start_node_cj)
    else:
        append_bar(start_node_cj + val_to_add, start_node_cj + 3 + val_to_add)
        append_bar(start_node_cj + 1 + val_to_add, start_node_cj + 2 + val_to_add)


def create_support():
    support_start = len(nodes)
    for i in range(SEGMENTS + 1):
        # create required nodes
        if i == 0:
            nodes.append([1/2 * TOWER_WIDTH - i * TOWER_WIDTH, 1/2 * TOWER_WIDTH, START_HEIGHT + 3/4 * SEGMENT_LENGTH])
        else:
            nodes.append([1/2 * TOWER_WIDTH - i * TOWER_WIDTH, 1/2 * TOWER_WIDTH, START_HEIGHT + 1/2 * SEGMENT_LENGTH])
        global NODES_FLOAT
        NODES_FLOAT = numpy.array(nodes).astype(float)
        # second batch
        if i == 1:
            # diagonal sections
            append_bar(END_NODE_TOWER, support_start + 1)
            append_bar(END_NODE_TOWER + 1, support_start + 1)
            append_bar(END_NODE_JIB, support_start + 1)
            append_bar(END_NODE_JIB + 1, support_start + 1)
            # top section
            append_bar(support_start, support_start + 1)
        # the rest
        else:
            if i == 0:
                start_node = END_NODE_TOWER
                append_bar(END_NODE_TOWER + 4, support_start)
            else:
                start_node = END_NODE_JIB
                append_bar(support_start + (i - 1), support_start + i)
            # diagonal sections
            val_to_add = max(3 * (i - 2), 0)
            append_bar(0 + start_node + val_to_add, support_start + i)
            append_bar(1 + start_node + val_to_add, support_start + i)
            append_bar(2 + start_node + val_to_add, support_start + i)
            append_bar(3 + start_node + val_to_add, support_start + i)


def get_nodes():
    """Return the nodes of the tower as numpy array of type float64"""
    return numpy.array(nodes).astype(float)


def get_nodes_raw():
    """Returns the nodes of the tower in original format"""
    return nodes


def get_beams():
    """Return the beams of the tower as numpy array"""
    return numpy.array(beams)


def get_beams_raw():
    """Retuns the beams of the tower in original format"""
    return beams


def get_length():
    """Returns total length of all beams"""
    return TOTAL_LENGTH


def append_bar(start_node, end_node):
    """
    Creates a beam between 2 given points and adds the length to a running total
    
    Args:
    :param start_node: start node of the beam
    :param end_node: end node of the beam
    """
    beams.append([start_node, end_node])
    global TOTAL_LENGTH
    TOTAL_LENGTH += numpy.linalg.norm(NODES_FLOAT[end_node] - NODES_FLOAT[start_node])
