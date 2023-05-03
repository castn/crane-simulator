"""
Provides all functions to build a crane
"""


import tower
import jib
import counter_jib

nodes = []
beams = []
tower_num_nodes = 0


def create_crane():
    """Creates all elements of the crane connected to each other"""
    create_tower()
    create_jib()
    create_counter_jib()


def create_tower():
    """Creates a tower"""
    tower.create(2, True, True, tower.Style.DIAGONAL)
    global tower_num_nodes
    tower_num_nodes = len(tower.get_nodes())
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
    jib.create_connected(tower.get_nodes_raw().copy(), tower.get_beams_raw().copy(), 4000, 2000, 4000, 2)
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
    counter_jib.create_connected(jib.get_nodes_raw().copy(), jib.get_beams_raw().copy(), 4000, 2000, tower_num_nodes, 4000)
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
