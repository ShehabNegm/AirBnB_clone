#!/usr/bin/python3
# test_amenity.py
"""unittesting for BaseModel subclass Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test class for Amenity subclass"""

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_is_BaseModel_subclass(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_created_at(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_amenity_updated_at(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_id(self):
        self.assertIsInstance(self.amenity.id, str)
        self.assertNotEqual(self.amenity.id, "")

    def test_amenity_save(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_amenity_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)
        self.assertIsInstance(amenity_dict['id'], str)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.amenity.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_amenity_name(self):
        name = "Swimming Pools"
        self.amenity.name = name
        self.assertEqual(self.amenity.name, "Swimming Pools")
        self.assertIsInstance(self.amenity.name, str)
