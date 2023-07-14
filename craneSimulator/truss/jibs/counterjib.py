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
    Enum to define a style how the support of the counterjib is built
    Can be TRUSS or TOWER
    """
    NOT_CHOSEN = 0
    TRUSS = 1
    TOWER = 2


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
    END_CJ_BASE = 0
    JIB_SEGMENTS = 0

    IS_CONNECTED = False

    TOTAL_LENGTH = 0
    LONGEST_BEAM = 0


def create():
    """Creates a counterjib separatley from the other components of the crane"""
    create_segments()
    create_beams()
    create_support()


def create_connected(crane_nodes, crane_beams, tower_height, tower_width, tower_num_nodes, jib_segments):
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
    Dims.JIB_SEGMENTS = jib_segments

    create_segments()
    create_beams()
    Dims.END_CJ_BASE = len(Comps.nodes)
    create_support()
    Dims.END_CJ = len(Comps.nodes)


def create_segments():
    """Creates all beams needed for the counterjib"""
    for i in range(Dims.SEGMENTS + 1):
        # skips the first run-through if nodes already exist
        if not (i == 0 and Dims.IS_CONNECTED):
            Comps.nodes.append([- Dims.SEGMENT_LENGTH * i, 0, Dims.START_HEIGHT])
            Comps.nodes.append([- Dims.SEGMENT_LENGTH * i,
                         Dims.TOWER_WIDTH, Dims.START_HEIGHT])


def create_beams():
    """Creates all beams needed for the counterjib"""
    start_node_cj = Dims.END_NODE_JIB  # len(nodes)
    if not Dims.IS_CONNECTED:
        append_beam(0, 1, True)
    for i in range(Dims.SEGMENTS):
        val_to_add = 2 * (i - 1)
        create_frame_beams(i, start_node_cj, val_to_add)
        create_diag_beams(i, start_node_cj, val_to_add)


def create_frame_beams(i, start_node_cj, val_to_add):
    """Creates the outer frame of the counterjib"""
    if i == 0:
        append_beam(Dims.END_NODE_TOWER, start_node_cj, True)
        append_beam(Dims.END_NODE_TOWER + 1, start_node_cj + 1, True)
    else:
        append_beam(start_node_cj + val_to_add, start_node_cj + 2 + val_to_add
                    , True)
        append_beam(start_node_cj + 1 + val_to_add,
                    start_node_cj + 3 + val_to_add, True)
    append_beam(start_node_cj + val_to_add + 2,
                start_node_cj + 1 + val_to_add + 2, True)


def create_diag_beams(i, start_node_cj, val_to_add):
    """Creates the diagonal beams of the counterjib"""
    if i == 0:
        append_beam(Dims.END_NODE_TOWER, start_node_cj + 1, True)
        append_beam(Dims.END_NODE_TOWER + 1, start_node_cj, True)
    else:
        append_beam(start_node_cj + val_to_add, start_node_cj + 3 + val_to_add
                    , True)
        append_beam(start_node_cj + 1 + val_to_add,
                    start_node_cj + 2 + val_to_add, True)


def create_support():
    """Creates appropriate support structure for the counterjib"""
    if Dims.SUPPORT_TYPE == Style.TRUSS:
        create_truss_support()
    elif Dims.SUPPORT_TYPE == Style.TOWER:
        create_tower_support()


def create_none_support():
    """Creates support of style 'none'"""
    #add pyramid on tower
    Comps.nodes.append([1/2 * Dims.TOWER_WIDTH,
                        1/2 * Dims.TOWER_WIDTH,
                        Dims.START_HEIGHT + Dims.HEIGHT])
    append_beam(Dims.END_NODE_TOWER + 4, Dims.END_CJ_BASE, True)
    append_beam(0 + Dims.END_NODE_TOWER, Dims.END_CJ_BASE, True)
    append_beam(1 + Dims.END_NODE_TOWER, Dims.END_CJ_BASE, True)
    append_beam(2 + Dims.END_NODE_TOWER, Dims.END_CJ_BASE, True)
    append_beam(3 + Dims.END_NODE_TOWER, Dims.END_CJ_BASE, True)
    #reinforce base
    append_beam(Dims.END_NODE_TOWER + 1, Dims.END_CJ_BASE - 2, False)
    append_beam(Dims.END_NODE_TOWER, Dims.END_CJ_BASE - 1, False)


def create_truss_support():
    """Creates truss style support structure for the counterjib"""
    support_start = Dims.END_CJ_BASE
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
            append_beam(Dims.END_NODE_TOWER, support_start + 1, True)
            append_beam(Dims.END_NODE_TOWER + 1, support_start + 1, True)
            append_beam(Dims.END_NODE_JIB, support_start + 1, True)
            append_beam(Dims.END_NODE_JIB + 1, support_start + 1, True)
            # top section
            append_beam(support_start, support_start + 1, True)
        # the rest
        else:
            if i == 0:
                start_node = Dims.END_NODE_TOWER
                append_beam(Dims.END_NODE_TOWER + 4, support_start, True)
            else:
                start_node = Dims.END_NODE_JIB - max(i - 2, 0)
                append_beam(support_start + (i - 1), support_start + i, True)
            # diagonal sections
            val_to_add = max(3 * (i - 2), 0)
            append_beam(0 + start_node + val_to_add, support_start + i, True)
            append_beam(1 + start_node + val_to_add, support_start + i, True)
            append_beam(2 + start_node + val_to_add, support_start + i, True)
            append_beam(3 + start_node + val_to_add, support_start + i, True)


def create_cable_support(one_tower):
    """Creates a cable style support for the counterjib"""
    cable_start = Dims.END_CJ_BASE
    if one_tower:
        Comps.nodes.append([Dims.TOWER_WIDTH / 2, Dims.TOWER_WIDTH /
                     2, Dims.START_HEIGHT + Dims.TOWER_WIDTH])
        # tower to new top
        for i in range(4):
            append_beam(Dims.END_NODE_TOWER + i, cable_start, True)
        # jib to new top
        append_beam(Dims.END_NODE_TOWER + 4, cable_start, True)
        # new top to end counterjib
        append_beam(cable_start, cable_start - 1, False)
        append_beam(cable_start, cable_start - 2, False)
    else:
        Comps.nodes.append([Dims.TOWER_WIDTH / 2, 0,
                     Dims.START_HEIGHT + Dims.TOWER_WIDTH])
        Comps.nodes.append([Dims.TOWER_WIDTH / 2, Dims.TOWER_WIDTH,
                     Dims.START_HEIGHT + Dims.TOWER_WIDTH])
        # tower to new tops
        for i in range(2):
            append_beam(Dims.END_NODE_TOWER + i, cable_start + i, True)
            append_beam(Dims.END_NODE_TOWER + i + 2, cable_start + i, True)
        # between new tops
        append_beam(cable_start, cable_start + 1, True)
        # jib to new tops
        append_beam(Dims.END_NODE_TOWER + 4, cable_start, True)
        append_beam(Dims.END_NODE_TOWER + 4, cable_start + 1, True)
        # new tops to end counterjib
        append_beam(cable_start, cable_start - 2, False)
        append_beam(cable_start + 1, cable_start - 1, False)
    #reinforce base
    append_beam(Dims.END_NODE_TOWER + 1, Dims.END_CJ_BASE - 2, False)
    append_beam(Dims.END_NODE_TOWER, Dims.END_CJ_BASE - 1, False)
    append_beam(Dims.END_NODE_TOWER, Dims.END_CJ_BASE - 2, False)
    append_beam(Dims.END_NODE_TOWER + 1, Dims.END_CJ_BASE - 1, False)


def create_tower_support():
    """Creates a support in the style of a regular tower crane"""
    Comps.nodes.append([Dims.TOWER_WIDTH / 2, Dims.TOWER_WIDTH / 2,
                        Dims.START_HEIGHT + Dims.TOWER_WIDTH * 2])
    # Truss support
    support_start = Dims.END_CJ_BASE
    for i in range(Dims.SEGMENTS + 1):
        # create required nodes
        if i != 0:
            Comps.nodes.append([- Dims.SEGMENT_LENGTH * ((i * 2) - 1) / 2,
                                1/2 * Dims.TOWER_WIDTH,
                                Dims.START_HEIGHT + Dims.HEIGHT])
        # second batch
        if i == 1:
            # diagonal sections
            append_beam(Dims.END_NODE_TOWER, support_start + 1, True)
            append_beam(Dims.END_NODE_TOWER + 1, support_start + 1, True)
            append_beam(Dims.END_NODE_JIB, support_start + 1, True)
            append_beam(Dims.END_NODE_JIB + 1, support_start + 1, True)
        # the rest
        else:
            if i == 0:
                start_node = Dims.END_NODE_TOWER
                # append_beam(Dims.END_NODE_TOWER + 4, support_start, True)
            else:
                start_node = Dims.END_NODE_JIB - max(i - 2, 0)
                append_beam(support_start + (i - 1), support_start + i, True)
            # diagonal sections
            val_to_add = max(3 * (i - 2), 0)
            append_beam(0 + start_node + val_to_add, support_start + i, i != 0)
            append_beam(1 + start_node + val_to_add, support_start + i, i != 0)
            append_beam(2 + start_node + val_to_add, support_start + i, i != 0)
            append_beam(3 + start_node + val_to_add, support_start + i, i != 0)
    # Cables
    append_beam(support_start, support_start - 3, False)
    append_beam(support_start, support_start - 4, False)
    append_beam(support_start, int((Dims.END_NODE_JIB - Dims.END_NODE_TOWER) / 2
                                   + Dims.END_NODE_TOWER) + (2 if Dims.JIB_SEGMENTS % 2 == 0 else 4),
                False)


def append_beam(start_node, end_node, len_counts):
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
    if len_counts:
        Dims.LONGEST_BEAM = max(length, Dims.LONGEST_BEAM)
    Dims.TOTAL_LENGTH += length


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


def get_longest_beam():
    """Returns length of longest beam"""
    return Dims.LONGEST_BEAM


def get_support_type():
    """Returns support type of counterjib"""
    return Dims.SUPPORT_TYPE


def get_end_cj_base():
    """Returns last node of the base of the counterjib"""
    return Dims.END_CJ_BASE


def get_end_cj():
    """Returns last node of the counterjib"""
    return Dims.END_CJ


def set_dims(length, height, segs, sup_style):
    """Sets dimensions of the counterjib to passed-through values"""
    Comps.nodes = []
    Comps.beams = []
    Dims.TOTAL_LENGTH = 0
    Dims.LONGEST_BEAM = 0

    Dims.SEGMENTS = segs
    Dims.SEGMENT_LENGTH = length / segs
    Dims.HEIGHT = height
    if sup_style == 'Truss':
        Dims.SUPPORT_TYPE = Style.TRUSS
    elif sup_style == 'Tower':
        Dims.SUPPORT_TYPE = Style.TOWER


def default_dims():
    """Sets default parameters for the dimensions of the counterjib"""
    Dims.SEGMENTS = 2
    Dims.SEGMENT_LENGTH = 1000
    Dims.HEIGHT = 800
    Dims.SUPPORT_TYPE = Style.TRUSS
