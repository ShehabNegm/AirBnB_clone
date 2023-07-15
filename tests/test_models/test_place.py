#!/usr/bin/python3
# test_place.py
"""unittesting for BaseModel subclass Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unitest.TestCase):
    """Test class for Place subclass"""

    def setUp(self):
        self.place = Place()

    def test_place_is_BaseModel_subclass(self):
        self.assertIsInstance(Place(), BaseModel)

    def test_place_created_at(self):
        self.assertIsInstance(self.place.created_at, datetime)

    def test_place_updated_at(self):
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_place_id(self):
        self.assertIsInstance(self.place.id, str)
        self.assertNotEqual(self.place.id, "")

    def test_place_save(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_place_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.asertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertIsInstance(place_dict['id'], str)
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_place_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.place.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_place_name(self):
        name = "Cali"
        self.place.name = name
        self.assertEqual(self.place.name, "Cali")
        self.assertIsInstance(self.place.name, str)
