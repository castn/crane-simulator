"""
Provides all functions to build a crane
"""

import numpy as np

from craneSimulator.simulation import analysis
from craneSimulator.truss.jibs import jib, counterjib
from craneSimulator.truss.tower import tower

# Youngs Module
E = 210e9  # 210GPa
# Cross section of each beam
A = 0.01  # 0.01m^2
DENSITY = 7850

has_tower = True
has_jib = True
has_counter_jib = True


class Dims:
    """Class that contains all dimensions of the crane for global control"""
    TOWER_HEIGHT = 0
    TOWER_WIDTH = 0
    TOWER_NUM_NODES = 0


class Comps:
    """Component arrays for the crane"""
    nodes = []
    beams = []


def set_tower_dims(tower_height, tower_width, tower_segs, tower_sup_style):
    """Sets dimensions of the tower"""
    tower.set_dims(tower_height, tower_width, tower_segs, tower_sup_style)


def set_jib_dims(jib_length, jib_height, jib_segs):
    """Sets dimensions of the jib"""
    jib.set_dims(jib_length, jib_height, jib_segs)


def set_counterjib_dims(counterjib_length, counterjib_height, counterjib_segs, counterjib_sup_style):
    """Sets dimensions of the counterjib"""
    counterjib.set_dims(counterjib_length, counterjib_height, counterjib_segs, counterjib_sup_style)


def set_default_dims():
    """Sets default dimensions for all components"""
    tower.default_dims()
    jib.default_dims()
    counterjib.default_dims()


def build_crane():
    """Builds crane from previosuly inputted parameters"""
    if has_tower:
        create_tower()
    if has_jib:
        create_jib()
    if has_counter_jib:
        create_counterjib()


def create_crane():
    """Creates all elements of the crane connected to each other"""
    create_tower()
    create_jib()
    create_counterjib()


def create_tower():
    """Creates a tower"""
    tower.create(True, True)
    Dims.TOWER_HEIGHT, Dims.TOWER_WIDTH = tower.get_height_width()
    Dims.TOWER_NUM_NODES = len(tower.get_nodes())
    Comps.nodes = tower.get_nodes_raw().copy()
    Comps.beams = tower.get_beams_raw().copy()


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
    Comps.nodes = jib.get_nodes_raw().copy()
    Comps.beams = jib.get_beams_raw().copy()


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
    Comps.nodes = counterjib.get_nodes_raw().copy()
    Comps.beams = counterjib.get_beams_raw().copy()


def get_counterjib():
    """Returns the nodes and beams of the counterjib in converted formats"""
    return counterjib.get_nodes(), counterjib.get_beams()


def get_counterjib_length():
    """Returns the length of all beams used in the counterjib"""
    return counterjib.get_length()


def get_crane():
    """Returns the nodes and beams of the crane in converted formats"""
    return np.array(Comps.nodes).astype(float), np.array(Comps.beams)


def get_crane_raw():
    """Returns the raw nodes and beams of the crane"""
    return Comps.nodes, Comps.beams


def get_length():
    """Returns the length of all beams used in the crane"""
    return tower.get_length() + jib.get_length() + counterjib.get_length()


def should_have_tower(boolean):
    has_tower = boolean


def should_have_jib(boolean):
    has_jib = boolean


def should_have_counter_jib(boolean):
    has_counter_jib = boolean


def enable_gravity():
    """Applies gravity to nodes"""
    analysis.apply_gravity(Comps.nodes, Comps.beams, A, DENSITY)


def disable_gravity():
    """Removes gravity from nodes"""
    analysis.remove_gravity(Comps.nodes)


def analyze():
    """Performs the analysis of the crane"""
    analysis.generate_conditions(Comps.nodes)
    return analysis.analyze(Comps.nodes, Comps.beams, E, A)
