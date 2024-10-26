#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
