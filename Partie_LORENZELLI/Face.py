class Face:

    def __init__(self, color, type):
        self.__color = color
        self.__type = type

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type
