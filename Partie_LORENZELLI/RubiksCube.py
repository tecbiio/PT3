# -*- coding: utf-8 -*-
import numpy as np
import Movement

class RubiksCube:

    def __init__(self):
        tab = np.zeros((6,3,3))
        for i in range(0,6):
            tab[i,:,:] = i
        self.__tab = tab

    def get_tab(self):
        return self.__tab

    def set_tab(self, tab):
        self.__tab = tab

    def set_val_tab(self, index1, index2, index3, val):
        self.__tab[index1, index2, index3] = val
