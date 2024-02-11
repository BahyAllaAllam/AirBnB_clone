#!/usr/bin/python3
"""
Unit tests for the Review class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review

    def test_attributes_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_to_dict_returns_dict(self):
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.review.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at',
                         '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.review.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.review.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.review.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.review.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
