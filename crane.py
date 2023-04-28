import tower
import jib
import counter_jib

tower_num_nodes = 0


def create_crane():
    create_tower()
    create_jib()
    create_counter_jib()


def create_tower():
    tower.create(2, True, True, tower.Style.DIAGONAL)
    global tower_num_nodes
    tower_num_nodes = len(tower.get_nodes())


def get_tower():
    return tower.get_nodes(), tower.get_bars()


def get_tower_length():
    return tower.get_length()


def create_jib():
    jib.create_connected(tower.get_nodes_raw(), tower.get_bars_raw(), 4000, 2000, 4000, 2)


def get_jib():
    return jib.get_nodes(), jib.get_bars()


def get_jib_length():
    return jib.get_length()


def create_counter_jib():
    counter_jib.create_connected(jib.get_nodes_raw(), jib.get_bars_raw(), 4000, 2000, tower_num_nodes, 4000)


def get_counter_jib():
    return counter_jib.get_nodes(), counter_jib.get_bars()


def get_counter_jib_length():
    return counter_jib.get_length()


def get_length():
    return tower.get_length() + jib.get_length() + counter_jib.get_length()
