#!/usr/bin/python3
"""
Unit tests for the Amenity class
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_attributes_default_values(self):
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_to_dict_returns_dict(self):
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.amenity.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at',
                         '__class__', 'name']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.amenity.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.amenity.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.amenity.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
