#!/usr/bin/python3
import unittest
import os.path
from models.base import Base
"""tests the Base"""


class TestBase(unittest.TestCase):

    def test_id(self):
        """tests the ids"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_dictionary(self):
        """tests the dictionary"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_saveFile(self):
        """tests the savefile"""
        Base._Base__nb_objects = 0
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) > 1)
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) > 1)

        with open("Rectangle.json", 'r') as f:
            self.assertTrue(f.read() == "[]")
        with open("Square.json", 'r') as f:
            self.assertTrue(f.read() == "[]")

    def test_fromJson(self):
        """tests the fromjson"""
        r_input = [{'id': 89, 'width': 10, 'height': 4}]
        s_input = [{'id': 89, 'size': 4}]
       

      




if __name__ == '__main__':
    unittest.main()