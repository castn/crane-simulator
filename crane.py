"""
Provides all functions to build a crane
"""

import tower
import jib
import counterjib

nodes = []
beams = []


class Dims:
    """Class that contains all dimensions of the crane for global control"""
    TOWER_HEIGHT = 0
    TOWER_WIDTH = 0
    TOWER_NUM_NODES = 0


def set_tower_dims(tower_height, tower_width, tower_segs, tower_sup_style):
    """Sets dimensions of the tower"""
    print('Setting tower')
    tower.set_dims(tower_height, tower_width, tower_segs, tower_sup_style)


def set_jib_dims(jib_length, jib_height, jib_segs):
    """Sets dimensions of the jib"""
    print('Setting jib')
    jib.set_dims(jib_length, jib_height, jib_segs)


def set_counterjib_dims(counterjib_length, counterjib_height, counterjib_segs, counterjib_sup_style):
    """Sets dimensions of the counterjib"""
    print('Setting counterjib')
    counterjib.set_dims(counterjib_length, counterjib_height, counterjib_segs, counterjib_sup_style)


def build_crane():
    """Builds crane from previosuly inputted parameters"""
    create_tower()
    create_jib()
    create_counterjib()


def create_crane():
    """Creates all elements of the crane connected to each other"""
    custom_dims = 'no' # should be ''
    while custom_dims != 'yes' and custom_dims != 'no':
        custom_dims = str(
            input('Would you like to enter custom dimensions? ')).lower()
    if custom_dims == 'yes':
        tower.get_dims()
        jib.get_dims()
        counterjib.get_dims()
        print('Now generating custom crane')
    else:
        tower.default_dims()
        jib.default_dims()
        counterjib.default_dims()
        print('Now generating default crane')

    create_tower()
    create_jib()
    create_counterjib()


def create_tower():
    """Creates a tower"""
    tower.create(True, True, tower.Style.DIAGONAL)
    Dims.TOWER_HEIGHT, Dims.TOWER_WIDTH = tower.get_height_width()
    Dims.TOWER_NUM_NODES = len(tower.get_nodes())
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
    jib.create_connected(tower.get_nodes_raw().copy(), tower.get_beams_raw().copy(),
                         Dims.TOWER_HEIGHT, Dims.TOWER_WIDTH)
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


def create_counterjib():
    """Creates a counterjib connected to the other elements of the crane"""
    counterjib.create_connected(jib.get_nodes_raw().copy(), jib.get_beams_raw().copy(),
                                 Dims.TOWER_HEIGHT, Dims.TOWER_WIDTH, Dims.TOWER_NUM_NODES)
    # print(len(counterjib.get_nodes()))
    # global nodes
    # nodes = counterjib.get_nodes_raw()
    # global beams
    # beams = counterjib.get_beams_raw()
    # counterjib.create(2000, 4000)


def get_counterjib():
    """Returns the nodes and beams of the counterjib in converted formats"""
    return counterjib.get_nodes(), counterjib.get_beams()


def get_counterjib_length():
    """Returns the length of all beams used in the counterjib"""
    return counterjib.get_length()


def get_crane():
    """Returns the nodes and beams of the crane in converted formats"""
    return get_counterjib()


def get_length():
    """Returns the length of all beams used in the crane"""
    return tower.get_length() + jib.get_length() + counterjib.get_length()
