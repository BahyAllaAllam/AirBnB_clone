#!/usr/bin/python3
"""
Unit Tests for the FileStorage class
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = storage._FileStorage__file_path
        self.objects = storage._FileStorage__objects
        self.instance = BaseModel()
        self.instance.save()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        storage.reload()

    def test_attributes(self):
        self.assertEqual(self.file_path, "file.json")
        self.assertIsInstance(self.objects, dict)

    def test_all(self):
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(
            type(self.instance).__name__ + '.' + self.instance.id, all_objects
        )

    def test_new(self):
        new_instance = BaseModel()
        new_instance_key = type(new_instance).__name__ + '.' + new_instance.id
        self.assertNotIn(new_instance_key, self.objects)
        storage.new(new_instance)
        self.assertIn(new_instance_key, self.objects)

    def test_save_reload(self):
        storage.save()
        with open(self.file_path, 'r') as f:
            data = f.read()
            self.assertNotEqual(data, '{}')
        storage.reload()
        all_objects = storage.all()
        self.assertIn(
            type(self.instance).__name__ + '.' + self.instance.id, all_objects
        )

    def test_get_classes(self):
        classes = storage.get_classes()
        self.assertIsInstance(classes, list)
        self.assertIn('BaseModel', classes)
        self.assertIn('User', classes)
        self.assertIn('State', classes)
        self.assertIn('City', classes)
        self.assertIn('Amenity', classes)
        self.assertIn('Place', classes)
        self.assertIn('Review', classes)


if __name__ == '__main__':
    unittest.main()
