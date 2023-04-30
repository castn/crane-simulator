"""
Provides all functions to build the counterjib of a crane
"""

import numpy

nodes = []
bars = []

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


def create_connected(crane_nodes, crane_bars, tower_height, tower_width, tower_num_nodes, length):
    """
    Creates a counterjib with desired dimensions connected to the rest of the crane
    
    Args:
    :param crane_nodes: array of nodes used by the crane
    :param crane_bars: array of beams used by the crane
    :param tower_height: height of the tower of the crane
    :param tower_width: width of the tower of the crane
    :param tower_num_nodes: number of nodes used to construct the tower
    :param length: desired length of the counterjib
    """
    global nodes
    nodes = crane_nodes
    global bars
    bars = crane_bars
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
        bars.append([0, 1])
        add_length(0, 1)
    for i in range(SEGMENTS):
        val_to_add = 2 * (i - 1)
        create_frame_beams(i, start_node_cj, val_to_add)
        create_diag_beams(i, start_node_cj, val_to_add)
        

def create_frame_beams(i, start_node_cj, val_to_add):
    """Creates the outer frame of the counterjib"""
    if i == 0:
        bars.append([END_NODE_TOWER, start_node_cj])
        add_length(END_NODE_TOWER, start_node_cj)
        bars.append([END_NODE_TOWER + 1, start_node_cj + 1])
        add_length(END_NODE_TOWER + 1, start_node_cj + 1)
    else:
        bars.append([start_node_cj + val_to_add, start_node_cj + 2 + val_to_add])
        add_length(start_node_cj + val_to_add, start_node_cj + 2 + val_to_add)
        bars.append([start_node_cj + 1 + val_to_add, start_node_cj + 3 + val_to_add])
        add_length(start_node_cj + 1 + val_to_add, start_node_cj + 3 + val_to_add)
    bars.append([start_node_cj + val_to_add + 2, start_node_cj + 1 + val_to_add + 2])
    add_length(start_node_cj + val_to_add + 2, start_node_cj + 1 + val_to_add + 2)


def create_diag_beams(i, start_node_cj, val_to_add):
    """Creates the diagonal beams of the counterjib"""
    if i == 0:
        bars.append([END_NODE_TOWER, start_node_cj + 1])
        add_length(END_NODE_TOWER, start_node_cj + 1)
        bars.append([END_NODE_TOWER + 1, start_node_cj])
        add_length(END_NODE_TOWER + 1, start_node_cj)
    else:
        bars.append([start_node_cj + val_to_add, start_node_cj + 3 + val_to_add])
        add_length(start_node_cj + val_to_add, start_node_cj + 3 + val_to_add)
        bars.append([start_node_cj + 1 + val_to_add, start_node_cj + 2 + val_to_add])
        add_length(start_node_cj + 1 + val_to_add, start_node_cj + 2 + val_to_add)


def get_nodes():
    """Return the nodes of the tower as numpy array of type float64"""
    return numpy.array(nodes).astype(float)


def get_nodes_raw():
    """Returns the nodes of the tower in original format"""
    return nodes


def get_bars():
    """Return the bars of the tower as numpy array"""
    return numpy.array(bars)


def get_bars_raw():
    """Retuns the bars of the tower in original format"""
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
    """Returns total length of all beams"""
    return TOTAL_LENGTH
