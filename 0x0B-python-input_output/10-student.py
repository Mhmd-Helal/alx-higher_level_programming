#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            my_dict = {}
            for i in self.__dict__:
                if i in attrs:
                    my_dict[i] = self.__dict__[i]
            return my_dict
            # return {x: y for x, y in self.__dict__.items() if x in attrs}
        return self.__dict__
