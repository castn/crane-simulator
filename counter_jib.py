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


def create_connected(crane_nodes, crane_bars, tower_height, tower_width, tower_num_nodes, length):
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
    
    create_segments()
    
    global NODES_FLOAT
    NODES_FLOAT = numpy.array(nodes).astype(float)
    
    create_beams()


def create_segments():
    for i in range(SEGMENTS + 1):
        if not (i == 0 and IS_CONNECTED):  # skips the first run-through if nodes already exist
            nodes.append([TOWER_WIDTH - SEGMENT_LENGTH * i, 0, START_HEIGHT])
            nodes.append([TOWER_WIDTH - SEGMENT_LENGTH * i, TOWER_WIDTH, START_HEIGHT])


def create_beams():
    start_node_cj = len(nodes)
    for i in range(SEGMENTS):
        val_to_add = 2 * i
        create_frame_beams(i, start_node_cj, val_to_add)
        create_diag_beams(i, start_node_cj, val_to_add)
    # before
    # 18 nodes
    # 45 bars -> 17 highest index
    # after
    # 22 nodes
    # 55 bars -> 27 highest index (should be 21)
        

def create_frame_beams(i, start_node_cj, val_to_add):
    if i == 0:
        bars.append([END_NODE_TOWER, start_node_cj])
        bars.append([END_NODE_TOWER + 1, start_node_cj + 1])
    else:
        bars.append([start_node_cj + val_to_add, start_node_cj + 2 + val_to_add])
        bars.append([start_node_cj + 1 + val_to_add, start_node_cj + 3 + val_to_add])
    bars.append([start_node_cj + 2 + val_to_add, start_node_cj + 3 + val_to_add])


def create_diag_beams(start_node_cj, val_to_add):
    bars.append([start_node_cj + val_to_add, start_node_cj + 3 + val_to_add])
    bars.append([start_node_cj + 1 + val_to_add, start_node_cj + 2 + val_to_add])


def get_nodes():
    """
    Return the nodes of tower as numpy array of type float64
    """
    return numpy.array(nodes).astype(float)


def get_bars():
    """Return the bars of tower as numpy array"""
    return numpy.array(bars)


def get_length():
    return 0
