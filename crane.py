"""
Provides all functions to build a crane
"""


import tower
import jib
import counter_jib

nodes = []
beams = []
TOWER_HEIGHT = 0
TOWER_WIDTH = 0
TOWER_NUM_NODES = 0


def create_crane(tower_height, tower_segs, tower_seg_height, tower_width):
    """Creates all elements of the crane connected to each other"""
    create_tower(tower_height, tower_segs, tower_seg_height, tower_width)
    create_jib()
    create_counter_jib()


def create_tower(tower_height, tower_segs, tower_seg_height, tower_width):
    """Creates a tower"""
    tower.create(tower_segs, tower_seg_height, tower_width, True, True, tower.Style.DIAGONAL)
    global TOWER_HEIGHT
    TOWER_HEIGHT = tower_height
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global TOWER_NUM_NODES
    TOWER_NUM_NODES = len(tower.get_nodes())
    # global nodes
    # nodes = tower.get_nodes_raw()
    # global beams
    # beams = tower.get_beams_raw()


def get_tower():
    """Returns the nodes and beams of the tower in converted formats"""
    return tower.get_nodes(), tower.get_beams()


def get_tower_length():
    """Returns the length of all beams used in the tower"""
    return tower.get_length()


def create_jib():
    """Creates a jib connected to the other elements of the crane"""
    jib.create_connected(tower.get_nodes_raw().copy(), tower.get_beams_raw().copy(), TOWER_HEIGHT, TOWER_WIDTH, TOWER_HEIGHT, 2)
    # print(len(jib.get_nodes()))
    # global nodes
    # nodes = jib.get_nodes_raw()
    # global beams
    # beams = jib.get_beams_raw()


def get_jib():
    """Returns the nodes and beams of the jib in converted formats"""
    return jib.get_nodes(), jib.get_beams()


def get_jib_length():
    """Returns the length of all beams used in the jib"""
    return jib.get_length()


def create_counter_jib():
    """Creates a counterjib connected to the other elements of the crane"""
    counter_jib.create_connected(jib.get_nodes_raw().copy(), jib.get_beams_raw().copy(), TOWER_HEIGHT, TOWER_WIDTH, TOWER_NUM_NODES, 2, TOWER_HEIGHT)
    # print(len(counter_jib.get_nodes()))
    # global nodes
    # nodes = counter_jib.get_nodes_raw()
    # global beams
    # beams = counter_jib.get_beams_raw()
    # counter_jib.create(2000, 4000)


def get_counter_jib():
    """Returns the nodes and beams of the counterjib in converted formats"""
    return counter_jib.get_nodes(), counter_jib.get_beams()


def get_counter_jib_length():
    """Returns the length of all beams used in the counterjib"""
    return counter_jib.get_length()


def get_crane():
    """Returns the nodes and beams of the crane in converted formats"""
    return get_counter_jib()


def get_length():
    """Returns the length of all beams used in the crane"""
    return tower.get_length() + jib.get_length() + counter_jib.get_length()
