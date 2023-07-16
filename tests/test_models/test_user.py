#!/usr/bin/python3
"""unittesting for subclass User of BaseModel"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """unittest for User class of BaseModel"""

    def setUp(self):
        self.user = User()

    def test_user_BaseModel(self):
        self.assertIsInstance(User(), BaseModel)

    def test_user_created_at(self):
        self.assertIsInstance(self.user.created_at, datetime)

    def test_user_updated_at(self):
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_id(self):
        self.assertIsInstance(self.user.id, str)

    def test_user_id_2(self):
        id = self.user.id
        self.assertEqual(id, self.user.id)

    def test_user_save_update(self):
        update1 = self.user.updated_at
        self.user.save()
        update2 = self.user.updated_at
        self.assertNotEqual(update1, update2)

    def test_user_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.user.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_user_to_dict_values(self):
        dic_object = self.user.to_dict()
        my_new_model = User(**dic_object)
        self.assertIsInstance(my_new_model.id, str)
        self.assertEqual(my_new_model.id, self.user.id)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)

    def test_user_email(self):
        email = "test@test.com"
        self.user.email = email
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "test@test.com")

    def test_user_passwrod(self):
        password = "12345"
        self.user.password = password
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "12345")

    def test_user_first_name(self):
        first_name = "lol"
        self.user.first_name = first_name
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "lol")

    def test_user_last_name(self):
        last_name = "nah"
        self.user.last_name = last_name
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "nah")


if __name__ == "__main__":
    unittest.main()
