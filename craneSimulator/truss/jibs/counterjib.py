"""
Provides all functions to build the counterjib of a crane
"""

from enum import Enum
import numpy as np


class Comps:
    """Component arrays for the counterjib"""
    nodes = []
    beams = []


class Style(Enum):
    """
    Enum to define a style how the beams of the tower are placed.
    Can be PARALLEL, CROSS or ZIGZAG
    """
    NOT_CHOSEN = 0
    NONE = 1
    TRUSS = 2
    ONE_TOWER = 3
    TWO_TOWER = 4


class Dims:
    """Class that contains all dimensions of the counterjib for global control"""
    SEGMENT_LENGTH = 0
    SEGMENTS = 0
    HEIGHT = 0
    SUPPORT_TYPE = Style.NOT_CHOSEN

    START_HEIGHT = 0
    TOWER_WIDTH = 0
    END_NODE_TOWER = 0
    END_NODE_JIB = 2
    END_CJ = 0

    IS_CONNECTED = False

    TOTAL_LENGTH = 0


def create():
    """Creates a counterjib separatley from the other components of the crane"""
    create_segments()
    create_beams()
    create_support()


def create_connected(crane_nodes, crane_beams, tower_height, tower_width, tower_num_nodes):
    """
    Creates a counterjib with desired dimensions connected to the rest of the crane

    Args:
    :param crane_nodes: array of nodes used by the crane
    :param crane_beams: array of beams used by the crane
    :param tower_height: height of the tower of the crane
    :param tower_width: width of the tower of the crane
    :param tower_num_nodes: number of nodes used to construct the tower
    """
    Comps.nodes = crane_nodes
    Comps.beams = crane_beams

    Dims.START_HEIGHT = tower_height
    Dims.TOWER_WIDTH = tower_width
    Dims.IS_CONNECTED = True
    Dims.END_NODE_TOWER = tower_num_nodes - 4
    Dims.END_NODE_JIB = len(crane_nodes)

    create_segments()
    create_beams()
    create_support()


def create_segments():
    """Creates all beams needed for the counterjib"""
    for i in range(Dims.SEGMENTS + 1):
        # skips the first run-through if nodes already exist
        if not (i == 0 and Dims.IS_CONNECTED):
            Comps.nodes.append([- Dims.SEGMENT_LENGTH * i, 0, Dims.START_HEIGHT])
            Comps.nodes.append([- Dims.SEGMENT_LENGTH * i,
                         Dims.TOWER_WIDTH, Dims.START_HEIGHT])
    Dims.END_CJ = len(Comps.nodes)


def create_beams():
    """Creates all beams needed for the counterjib"""
    start_node_cj = Dims.END_NODE_JIB  # len(nodes)
    if not Dims.IS_CONNECTED:
        append_beam(0, 1)
    for i in range(Dims.SEGMENTS):
        val_to_add = 2 * (i - 1)
        create_frame_beams(i, start_node_cj, val_to_add)
        create_diag_beams(i, start_node_cj, val_to_add)


def create_frame_beams(i, start_node_cj, val_to_add):
    """Creates the outer frame of the counterjib"""
    if i == 0:
        append_beam(Dims.END_NODE_TOWER, start_node_cj)
        append_beam(Dims.END_NODE_TOWER + 1, start_node_cj + 1)
    else:
        append_beam(start_node_cj + val_to_add, start_node_cj + 2 + val_to_add)
        append_beam(start_node_cj + 1 + val_to_add,
                    start_node_cj + 3 + val_to_add)
    append_beam(start_node_cj + val_to_add + 2,
                start_node_cj + 1 + val_to_add + 2)


def create_diag_beams(i, start_node_cj, val_to_add):
    """Creates the diagonal beams of the counterjib"""
    if i == 0:
        append_beam(Dims.END_NODE_TOWER, start_node_cj + 1)
        append_beam(Dims.END_NODE_TOWER + 1, start_node_cj)
    else:
        append_beam(start_node_cj + val_to_add, start_node_cj + 3 + val_to_add)
        append_beam(start_node_cj + 1 + val_to_add,
                    start_node_cj + 2 + val_to_add)


def create_support():
    """Creates appropriate support structure for the counterjib"""
    if Dims.SUPPORT_TYPE == Style.NONE:
        return
    elif Dims.SUPPORT_TYPE == Style.TRUSS:
        create_truss_support()
    elif Dims.SUPPORT_TYPE == Style.ONE_TOWER:
        create_cable_support(True)
    elif Dims.SUPPORT_TYPE == Style.TWO_TOWER:
        create_cable_support(False)


def create_truss_support():
    """Creates truss style support structure for the counterjib"""
    support_start = len(Comps.nodes)
    for i in range(Dims.SEGMENTS + 1):
        # create required nodes
        if i == 0:
            Comps.nodes.append([1/2 * Dims.TOWER_WIDTH - i * Dims.TOWER_WIDTH,
                                1/2 * Dims.TOWER_WIDTH,
                                Dims.START_HEIGHT + Dims.HEIGHT])
        else:
            Comps.nodes.append([- Dims.SEGMENT_LENGTH * ((i * 2) - 1) / 2,
                                1/2 * Dims.TOWER_WIDTH,
                                Dims.START_HEIGHT + Dims.HEIGHT])
        # second batch
        if i == 1:
            # diagonal sections
            append_beam(Dims.END_NODE_TOWER, support_start + 1)
            append_beam(Dims.END_NODE_TOWER + 1, support_start + 1)
            append_beam(Dims.END_NODE_JIB, support_start + 1)
            append_beam(Dims.END_NODE_JIB + 1, support_start + 1)
            # top section
            append_beam(support_start, support_start + 1)
        # the rest
        else:
            if i == 0:
                start_node = Dims.END_NODE_TOWER
                append_beam(Dims.END_NODE_TOWER + 4, support_start)
            else:
                start_node = Dims.END_NODE_JIB - max(i - 2, 0)
                append_beam(support_start + (i - 1), support_start + i)
            # diagonal sections
            val_to_add = max(3 * (i - 2), 0)
            append_beam(0 + start_node + val_to_add, support_start + i)
            append_beam(1 + start_node + val_to_add, support_start + i)
            append_beam(2 + start_node + val_to_add, support_start + i)
            append_beam(3 + start_node + val_to_add, support_start + i)


def create_cable_support(one_node):
    """Creates a cable style support for the counterjib"""
    cable_start = len(Comps.nodes)
    if one_node:
        Comps.nodes.append([Dims.TOWER_WIDTH / 2, Dims.TOWER_WIDTH /
                     2, Dims.START_HEIGHT + Dims.TOWER_WIDTH])
        # tower to new top
        for i in range(4):
            append_beam(Dims.END_NODE_TOWER + i, cable_start)
        # jib to new top
        append_beam(Dims.END_NODE_TOWER + 4, cable_start)
        # new top to end counterjib
        append_beam(cable_start, cable_start - 1)
        append_beam(cable_start, cable_start - 2)
    else:
        Comps.nodes.append([Dims.TOWER_WIDTH / 2, 0,
                     Dims.START_HEIGHT + Dims.TOWER_WIDTH])
        Comps.nodes.append([Dims.TOWER_WIDTH / 2, Dims.TOWER_WIDTH,
                     Dims.START_HEIGHT + Dims.TOWER_WIDTH])
        # tower to new tops
        for i in range(2):
            append_beam(Dims.END_NODE_TOWER + i, cable_start + i)
            append_beam(Dims.END_NODE_TOWER + i + 2, cable_start + i)
        # between new tops
        append_beam(cable_start, cable_start + 1)
        # jib to new tops
        append_beam(Dims.END_NODE_TOWER + 4, cable_start)
        append_beam(Dims.END_NODE_TOWER + 4, cable_start + 1)
        # new tops to end counterjib
        append_beam(cable_start, cable_start - 2)
        append_beam(cable_start + 1, cable_start - 1)


def get_nodes():
    """Return the nodes of the tower as numpy array of type float64"""
    return np.array(Comps.nodes).astype(float)


def get_nodes_raw():
    """Returns the nodes of the tower in original format"""
    return Comps.nodes


def get_beams():
    """Return the beams of the tower as numpy array"""
    return np.array(Comps.beams)


def get_beams_raw():
    """Retuns the beams of the tower in original format"""
    return Comps.beams


def get_length():
    """Returns total length of all beams"""
    return Dims.TOTAL_LENGTH


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
    Dims.TOTAL_LENGTH += np.linalg.norm(end_float - start_float)


def get_dims():
    """Prompts user to enter custom measurements for the counterjib in the console"""
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

    while Dims.SUPPORT_TYPE == Style.NOT_CHOSEN:
        sup_style = str(input(
            'What type of support would you like? Options include \'none\', \'truss\', \'single tower\', and \'twin tower\': ')).lower()
        if sup_style == 'none':
            Dims.SUPPORT_TYPE = Style.NONE
        elif sup_style == 'truss':
            Dims.SUPPORT_TYPE = Style.TRUSS
        elif sup_style == 'single tower':
            Dims.SUPPORT_TYPE = Style.ONE_TOWER
        elif sup_style == 'twin tower':
            Dims.SUPPORT_TYPE = Style.TWO_TOWER
        else:
            print('Sorry, that was not a valid input. Try again.')


def set_dims(length, height, segs, sup_style):
    """Sets dimensions of the counterjib to passed-through values"""
    Dims.SEGMENTS = segs
    Dims.SEGMENT_LENGTH = length / segs
    Dims.HEIGHT = height
    if sup_style == 'None':
        Dims.SUPPORT_TYPE = Style.NONE
    elif sup_style == 'Truss':
        Dims.SUPPORT_TYPE = Style.TRUSS
    elif sup_style == 'Single tower':
        Dims.SUPPORT_TYPE = Style.ONE_TOWER
    elif sup_style == 'Twin towers':
        Dims.SUPPORT_TYPE = Style.TWO_TOWER


def default_dims():
    """Sets default parameters for the dimensions of the counterjib"""
    Dims.SEGMENTS = 2
    Dims.SEGMENT_LENGTH = 1000
    Dims.HEIGHT = 800
    Dims.SUPPORT_TYPE = Style.TRUSS
