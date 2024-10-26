#!/usr/bin/python3
""" Append to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and
        returns the number of chars added"""
    with open(filename, "a", encoding='UTF-8') as f:
        return f.write(text)
