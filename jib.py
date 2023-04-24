import numpy

nodes = []
bars = []

SEGMENT_LENGTH = 2000
START_HEIGHT = 0
TOWER_WIDTH = 0
SEGMENTS = 0


def create(tower_height, tower_width, length, segments):
    """
    Creates jib seperatly from the tower but with the ability to connect to it

    Args:
        tower_height (float): height of the tower
        tower_width (float): width of the tower
        length (float): length of the jib to be created
        segments (int): number of segments the jib should consist of
    """
    global START_HEIGHT
    START_HEIGHT = tower_height
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global SEGMENT_LENGTH
    SEGMENT_LENGTH = length / segments
    global SEGMENTS
    # SEGMENTS = int(length / SEGMENT_LENGTH)
    SEGMENTS = segments
    global is_connected
    is_connected = False
    
    create_segments()
    create_beams()


def create_connected(tower_nodes, tower_bars, length, segments):
    """
    Creates jib attached to the tower as to have the entire crane in one block

    Args:
        tower_nodes (float[]): nodes which make up the tower
        tower_bars (int[]): bars which make up the tower
        length (float): length of the jib to be created
        segments (int): number of segments the jib should consist of
    """
    global nodes
    nodes = tower_nodes
    global bars
    bars = tower_bars
    global SEGMENT_LENGTH
    SEGMENT_LENGTH = length / segments
    global SEGMENTS
    SEGMENTS = segments
    global is_connected
    is_connected = True
    
    create_segments()
    create_beams()


def create_segments():
    for i in range(SEGMENTS + 1):
        if (not(i == 0 and is_connected)): # skips the first runthrough if nodes already exist (i hope)
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, 0, START_HEIGHT])
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, TOWER_WIDTH, START_HEIGHT])
        if (i < SEGMENTS):
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i  + SEGMENT_LENGTH / 2 , SEGMENT_LENGTH / 2, START_HEIGHT + SEGMENT_LENGTH])


def create_beams():
    for i in range(SEGMENTS):
        create_horz_beams(len(bars) + i)
        create_diag_beams(len(bars) + i)


def create_horz_beams(i):
    # connects all base nodes
    if (i == 0 and not(is_connected)):
        bars.append([0 + 3 * i, 1 + 3 * i]) # first horizontal (0-1) 
    if (i < SEGMENTS - 1):
        bars.append([2 + 3 * i, 5 + 3 * i]) # top connection
    bars.append([1 + 3 * i, 4 + 3 * i])
    bars.append([4 + 3 * i, 3 + 3 * i])
    bars.append([3 + 3 * i, 0 + 3 * i])
    bars.append([1 + 3 * i, 3 + 3 * i]) # diagonal beam


def create_diag_beams(i):
    # connects base nodes to top of pyramid
    bars.append([0 + 3 * i, 2 + 3 * i])
    bars.append([1 + 3 * i, 2 + 3 * i])
    bars.append([4 + 3 * i, 2 + 3 * i])
    bars.append([3 + 3 * i, 2 + 3 * i])


def get_nodes():
    return numpy.array(nodes).astype(float)


def get_bars():
    return numpy.array(bars)
    