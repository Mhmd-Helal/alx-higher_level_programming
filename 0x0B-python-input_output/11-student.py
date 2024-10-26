#!/usr/bin/python3
"""Student to disk and reload"""


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
            return {x: y for x, y in self.__dict__.items() if x in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if (json):
            self.__dict__ = json
