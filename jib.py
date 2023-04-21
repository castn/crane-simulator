import numpy

nodes = []
bars = []


def create():
    nodes.append([0, 0, 0])
    nodes.append([0, 2000, 0])
    nodes.append([0, 1000, 2000])

    nodes.append([500, 0, 0])
    nodes.append([500, 2000, 0])
    nodes.append([500, 1000, 2000])

    bars.append([0, 1])
    bars.append([1, 2])
    bars.append([0, 2])

    bars.append([3, 4])
    bars.append([4, 5])
    bars.append([3, 5])


def get_nodes():

    return numpy.array(nodes).astype(float)


def get_bars():
    return numpy.array(bars)
