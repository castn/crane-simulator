class Dims:
    # Variable definition
    TOWER_HEIGHT = 0
    TOWER_WIDTH = 0
    TOWER_SEGMENTS = 0
    TOWER_SUP_TYPE = 0

    JIB_HEIGHT = 0
    JIB_LENGTH = 0
    JIB_SEGMENTS = 0
    JIB_SUP_TYPE = 0

    COUNTERJIB_HEIGHT = 0
    COUNTERJIB_LENGTH = 0
    COUNTERJIB_SEGMENTS = 0
    COUNTERJIB_SUP_TYPE = 0

    def clear_all(self):
        self.clear_tower()
        self.clear_jib()
        self.clear_counter_jib()

    def clear_counter_jib(self):
        self.COUNTERJIB_HEIGHT = 0
        self.COUNTERJIB_LENGTH = 0
        self.COUNTERJIB_SEGMENTS = 0
        self.COUNTERJIB_SUP_TYPE = 0

    def clear_jib(self):
        self.JIB_HEIGHT = 0
        self.JIB_LENGTH = 0
        self.JIB_SEGMENTS = 0
        self.JIB_SUP_TYPE = 0

    def clear_tower(self):
        self.TOWER_HEIGHT = 0
        self.TOWER_WIDTH = 0
        self.TOWER_SEGMENTS = 0
        self.TOWER_SUP_TYPE = 0

    # Tower
    def get_tower_height(self):
        return self.TOWER_HEIGHT

    def get_tower_width(self):
        return self.TOWER_WIDTH

    def get_tower_segments(self):
        return self.TOWER_SEGMENTS

    def get_tower_segment_length(self):
        if self.TOWER_SEGMENTS == 0:
            return 0
        else:
            return self.TOWER_HEIGHT / self.TOWER_SEGMENTS

    def get_tower_support_type(self):
        return self.TOWER_SUP_TYPE

    def set_tower_height(self, height):
        self.TOWER_HEIGHT = height

    def set_tower_width(self, width):
        self.TOWER_WIDTH = width

    def set_tower_segments(self, segments):
        self.TOWER_SEGMENTS = segments

    def set_tower_support_type(self, support_type):
        self.TOWER_SUP_TYPE = support_type

    # Jib
    def get_jib_height(self):
        return self.JIB_HEIGHT

    def get_jib_length(self):
        return self.JIB_LENGTH

    def get_jib_segments(self):
        return self.JIB_SEGMENTS

    def get_jib_segment_length(self):
        if self.JIB_SEGMENTS == 0:
            return 0
        else:
            return self.JIB_LENGTH / self.JIB_SEGMENTS

    def get_jib_support_type(self):
        return self.JIB_SUP_TYPE

    def set_jib_height(self, height):
        self.JIB_HEIGHT = height

    def set_jib_length(self, length):
        self.JIB_LENGTH = length

    def set_jib_segments(self, segments):
        self.JIB_SEGMENTS = segments

    def set_jib_support_type(self, support_type):
        self.JIB_SUP_TYPE = support_type

    # Counter Jib
    def get_counter_jib_height(self):
        return self.COUNTERJIB_HEIGHT

    def get_counter_jib_length(self):
        return self.COUNTERJIB_LENGTH

    def get_counter_jib_segments(self):
        return self.COUNTERJIB_SEGMENTS

    def get_counter_jib_segment_length(self):
        if self.COUNTERJIB_LENGTH == 0:
            return 0
        else:
            return self.COUNTERJIB_LENGTH / self.COUNTERJIB_LENGTH

    def get_counter_jib_support_type(self):
        return self.COUNTERJIB_SUP_TYPE

    def set_counter_jib_height(self, height):
        self.COUNTERJIB_HEIGHT = height

    def set_counter_jib_length(self, length):
        self.COUNTERJIB_LENGTH = length

    def set_counter_jib_segments(self, segments):
        self.COUNTERJIB_SEGMENTS = segments

    def set_counter_jib_support_type(self, support_type):
        self.COUNTERJIB_SUP_TYPE = support_type
