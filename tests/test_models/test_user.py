#!/usr/bin/python3
"""
Unit tests for the User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_attributes_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_to_dict_returns_dict(self):
        obj_dict = self.user.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.user.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.user.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.user.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.user.to_dict()
        self.assertEqual(obj_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
