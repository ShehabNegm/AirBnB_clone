#!/usr/bin/python3
# test_city.py
"""unittesting for BaseModel subclass City"""
import unittest
from models.City import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unitest.TestCase):
    """Test class for City subclass"""

    def setUp(self):
        self.city = City()

    def test_city_is_BaseModel_subclass(self):
        self.assertIsInstance(City(), BaseModel)

    def test_city_created_at(self):
        self.assertIsInstance(self.city.created_at, datetime)

    def test_city_updated_at(self):
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_id(self):
        self.assertIsInstance(self.city.id, str)
        self.assertNotEqual(self.city.id, "")

    def test_city_save(self):
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_city_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.asertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertIsInstance(city_dict['id'], str)
        self.assertEqual(city_dict['__class__'], 'State')

    def test_city_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.city.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_city_name(self):
        name = "Cali"
        self.city.name = name
        self.assertEqual(self.city.name, "Cali")
        self.assertIsInstance(self.city.name, str)
