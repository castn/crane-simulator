import xml.etree.ElementTree as ET


def save_file(path, dictionary):
    data = ET.Element("data")
    config = ET.SubElement(data, "config")
    for item in dictionary:
        config_item = ET.SubElement(config, item)
        for value in dictionary.get(item):
            value_item = ET.SubElement(config_item, value)
            value_item.text = str(dictionary.get(item).get(value))

    data_as_string = str(ET.tostring(data))[1:].strip("'")
    if path.endswith(".xml"):
        file = open(path, "w")
    else:
        file = open(path + ".xml", "w")

    file.write('<?xml version="1.0"?>' + str(data_as_string))


class FileHandler():
    def __init__(self):
        self.config = None

    def load_file(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        config = dict()

        for child in root[0]:
            item = dict()
            for sub_child in child:
                item[sub_child.tag] = sub_child.text
            config[child.tag] = item

        self.config = config
