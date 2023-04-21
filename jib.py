import numpy

nodes = []
bars = []

SEGMENT_LENGTH = 2000
START_HEIGHT = 0
TOWER_WIDTH = 0
SEGMENTS = 0

def create(tower_height, tower_width, length):
    global START_HEIGHT
    START_HEIGHT = tower_height
    global TOWER_WIDTH
    TOWER_WIDTH = tower_width
    global SEGMENTS
    SEGMENTS = int(length / SEGMENT_LENGTH)
    
    print(SEGMENTS)
    
    create_segments()
    create_beams()
    
    T = 0
    # nodes.append([0, 0, 0])
    # nodes.append([0, 2000, 0])
    # nodes.append([0, 1000, 2000])

    # nodes.append([500, 0, 0])
    # nodes.append([500, 2000, 0])
    # nodes.append([500, 1000, 2000])

    # bars.append([0, 1])
    # bars.append([1, 2])
    # bars.append([0, 2])

    # bars.append([3, 4])
    # bars.append([4, 5])
    # bars.append([3, 5])

def create_segments():
    for i in range(SEGMENTS + 1):
        nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, 0, START_HEIGHT])
        nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i, TOWER_WIDTH, START_HEIGHT])
        if (i < SEGMENTS):
            nodes.append([TOWER_WIDTH + SEGMENT_LENGTH * i  + SEGMENT_LENGTH / 2 , SEGMENT_LENGTH / 2, START_HEIGHT + SEGMENT_LENGTH])

def create_beams():
    for i in range(SEGMENTS):
        create_horz_beams(i)
        create_diag_beams(i)
   
def create_horz_beams(i):
    # connects all base nodes
    if (i == 0):
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
    