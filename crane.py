import tower
import jib
import counter_jib

nodes = []
bars = []
tower_num_nodes = 0


def create_crane():
    create_tower()
    create_jib()
    create_counter_jib()


def create_tower():
    tower.create(2, True, True, tower.Style.DIAGONAL)
    global tower_num_nodes
    tower_num_nodes = len(tower.get_nodes())
    # global nodes
    # nodes = tower.get_nodes_raw()
    # global bars
    # bars = tower.get_bars_raw()


def get_tower():
    return tower.get_nodes(), tower.get_bars()


def get_tower_length():
    return tower.get_length()


def create_jib():
    jib.create_connected(tower.get_nodes_raw().copy(), tower.get_bars_raw().copy(), 4000, 2000, 4000, 2)
    # print(len(jib.get_nodes()))
    # global nodes
    # nodes = jib.get_nodes_raw()
    # global bars
    # bars = jib.get_bars_raw()


def get_jib():
    return jib.get_nodes(), jib.get_bars()


def get_jib_length():
    return jib.get_length()


def create_counter_jib():
    counter_jib.create_connected(jib.get_nodes_raw().copy(), jib.get_bars_raw().copy(), 4000, 2000, tower_num_nodes, 4000)
    print(len(counter_jib.get_nodes()))
    # global nodes
    # nodes = counter_jib.get_nodes_raw()
    # global bars
    # bars = counter_jib.get_bars_raw()
    # counter_jib.create(2000, 4000)


def get_counter_jib():
    return counter_jib.get_nodes(), counter_jib.get_bars()


def get_counter_jib_length():
    return counter_jib.get_length()


def get_crane():
    return 


def get_length():
    return tower.get_length() + jib.get_length() + counter_jib.get_length()
