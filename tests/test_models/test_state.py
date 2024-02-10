#!/usr/bin/python3
"""
Unit tests for the State class
"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_attributes_default_values(self):
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_to_dict_returns_dict(self):
        obj_dict = self.state.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.state.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at',
                         '__class__', 'name']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.state.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.state.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.state.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.state.to_dict()
        self.assertEqual(obj_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
