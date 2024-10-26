#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of char written"""
    with open(filename, "w", encoding='UTF-8') as f:
        return f.write(text)
