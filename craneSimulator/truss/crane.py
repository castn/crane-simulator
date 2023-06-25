"""
Provides all functions to build a crane
"""

import numpy as np

from craneSimulator.simulation import analysis
from craneSimulator.truss.jibs import jib, counterjib
from craneSimulator.truss.tower import tower


class Dims:
    """Class that contains all dimensions of the crane for global control"""
    TOWER_HEIGHT = 0
    TOWER_WIDTH = 0
    TOWER_NUM_NODES = 0
    JIB_NUM_NODES = 0


class Comps:
    """Component arrays for the crane"""
    nodes = []
    beams = []


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
    Dims.JIB_NUM_NODES = len(jib.get_nodes())
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


def create_crane():
    """Creates all elements of the crane connected to each other"""
    create_tower()
    create_jib()
    create_counterjib()


def set_tower_dims(tower_height, tower_width, tower_segs, tower_sup_style):
    """Sets dimensions of the tower"""
    tower.set_dims(tower_height, tower_width, tower_segs, tower_sup_style)


def set_jib_dims(jib_length, jib_height, jib_segs, jib_sup_type):
    """Sets dimensions of the jib"""
    jib.set_dims(jib_length, jib_height, jib_segs, jib_sup_type)


def set_counterjib_dims(counterjib_length, counterjib_height, counterjib_segs, counterjib_sup_style):
    """Sets dimensions of the counterjib"""
    counterjib.set_dims(counterjib_length, counterjib_height, counterjib_segs, counterjib_sup_style)


def set_default_dims():
    """Sets default dimensions for all components"""
    tower.default_dims()
    jib.default_dims()
    counterjib.default_dims()


class Crane:
    def __init__(self):
        self.E = 210e9  # Youngs module (210GPa)
        self.A = 0.0025  # Cross-section of beams (0.0025-0.0625m^2)
        self.DENSITY = 7850
        self.GRAVITY_CONSTANT = 9.81

        self.has_tower = True
        self.has_jib = True
        self.has_counter_jib = True

    def build_crane(self):
        """Builds crane from previosuly inputted parameters"""
        if self.has_tower:
            create_tower()
        if self.has_jib:
            create_jib()
        if self.has_counter_jib:
            create_counterjib()

    def enable_gravity(self, window):
        """Applies gravity to nodes"""
        analysis.apply_forces(window, Comps.nodes, Dims.TOWER_NUM_NODES, Dims.JIB_NUM_NODES)
        analysis.apply_gravity(np.array(Comps.nodes).astype(float), np.array(Comps.beams), self.A, self.DENSITY,
                               self.GRAVITY_CONSTANT)

    def reset_forces(self, window):
        """Resets forces on all nodes"""
        analysis.apply_forces(window, Comps.nodes, Dims.TOWER_NUM_NODES, Dims.JIB_NUM_NODES)

    def enable_wind(self, direc, force):
        """Applies wind in given direction with given force"""
        analysis.apply_wind(direc.lower(), force, counterjib.get_support_type(), counterjib.get_end_cj())

    def analyze(self):
        """Performs the analysis of the crane"""
        nodes, beams = get_crane()
        analysis.generate_conditions(nodes, beams)
        axial_force, reaction_force, deformation = analysis.analyze(nodes.copy(), beams.copy(), self.E, self.DENSITY)

        return axial_force, reaction_force, deformation, analysis.get_area_per_rod()

    def optimize(self):
        nodes, beams = get_crane()
        analysis.generate_conditions(nodes, beams)
        axial_force, reaction_force, deformation, area_per_rod = analysis.optimize(nodes.copy(), beams.copy(), self.E,
                                                                                   self.DENSITY)
        return axial_force, reaction_force, deformation, area_per_rod
