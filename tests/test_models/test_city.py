#!/usr/bin/python3
"""
Unit tests for the City class
"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_attributes_default_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_to_dict_returns_dict(self):
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.city.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at',
                         '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.city.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.city.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.city.to_dict()
        self.assertEqual(obj_dict['__class__'], 'City')

    def test_attributes_custom_values(self):
        custom_state_id = "CA"
        custom_name = "Los Angeles"

        self.city.state_id = custom_state_id
        self.city.name = custom_name

        self.assertEqual(self.city.state_id, custom_state_id)
        self.assertEqual(self.city.name, custom_name)


if __name__ == '__main__':
    unittest.main()
