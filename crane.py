import tower
import jib
import counter_jib


def get_tower():
    tower.create(2, True, True, tower.Style.DIAGONAL)
    return tower.get_nodes, tower.get_bars


def get_jib():
    jib.create_connected(tower.get_nodes_raw(), tower.get_bars_raw(), 4000, 2000, 4000, 2)
    return jib.get_nodes, jib.get_bars


def get_counter_jib():
    counter_jib.create()
    return counter_jib.get_nodes, counter_jib.get_bars