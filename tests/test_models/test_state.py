#!/usr/bin/python3
# test_state.py
"""unittesting for BaseModel subclass State"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Test class for State subclass"""

    def setUp(self):
        self.state = State()

    def test_state_is_BaseModel_subclass(self):
        self.assertIsInstance(State(), BaseModel)

    def test_state_created_at(self):
        self.assertIsInstance(self.state.created_at, datetime)

    def test_state_updated_at(self):
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_id(self):
        self.assertIsInstance(self.state.id, str)
        self.assertNotEqual(self.state.id, "")

    def test_state_save(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_state_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertIsInstance(state_dict['id'], str)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_state_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.state.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_state_name(self):
        name = "Cali"
        self.state.name = name
        self.assertEqual(self.state.name, "Cali")
        self.assertIsInstance(self.state.name, str)
