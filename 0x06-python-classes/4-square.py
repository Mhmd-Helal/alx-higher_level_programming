#!/usr/bin/python3
'''module doc'''


class Square:
    """
    creates square object
    """

    def __init__(self, size=0):
        self.size = size
    """
    initializes a square object with size
    Args:
        __size(int): size of square private property
    """
    @property
    def size(self):
        return self.__size
    """
    gets size of square
    """
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        sets size of square
        square must be integer and greater than 0
        """
    def area(self):
        return (self.__size**2)
        """
        return area of square based on size
        """
