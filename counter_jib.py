import numpy

nodes = []
bars = []


def create():
    create_segments()
    create_beams()


def create_segments():
    nodes.append[0, 0]
    nodes.append[1, 1]


def create_beams():
    bars.append[0, 1]


def get_nodes():
    """
    Return the nodes of tower as numpy array of type float64
    """
    return numpy.array(nodes).astype(float)


def get_bars():
    """Return the bars of tower as numpy array"""
    return numpy.array(bars)
