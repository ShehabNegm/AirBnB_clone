#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        updated_at_1 = self.base_model.updated_at
        self.base_model.save()
        updated_at_2 = self.base_model.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.base_model.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_to_dict_values(self):
        dic_object = self.base_model.to_dict()
        self.assertEqual(dic_object['id'], self.base_model.id)
        self.assertEqual(dic_object['updated_at'], self.base_model.updated_at)
        self.assertEqual(dic_object['created_at'], self.base_model.created_at)
        self.assertEqual(dic_object['__class__'],
                         self.base_model.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
