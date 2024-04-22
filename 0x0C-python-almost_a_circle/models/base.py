#!/usr/bin/python3
''' base module'''


class Base:
    ''' create a base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' if paramts == None increase __nb_objects and assign it to id'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
