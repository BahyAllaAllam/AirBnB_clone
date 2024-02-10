#!/usr/bin/python3
"""
Unit tests for the Place class
"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_attributes_default_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_to_dict_returns_dict(self):
        obj_dict = self.place.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.place.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__',
                         'city_id', 'user_id', 'name', 'description',
                         'number_rooms', 'number_bathrooms', 'max_guest',
                         'price_by_night', 'latitude', 'longitude',
                         'amenity_ids']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.place.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.place.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.place.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Place')


if __name__ == '__main__':
    unittest.main()
