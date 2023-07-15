#!/usr/bin/python3
# test_review.py
"""unittesting for BaseModel subclass Review"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Test class for State subclass"""

    def setUp(self):
        self.review = Reviw()

    def test_review_is_BaseModel_subclass(self):
        self.assertIsInstance(Review(), BaseModel)

    def test_review_created_at(self):
        self.assertIsInstance(self.review.created_at, datetime)

    def test_review_updated_at(self):
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_id(self):
        self.assertIsInstance(self.review.id, str)
        self.assertNotEqual(self.review.id, "")

    def test_review_save(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_review_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.asertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertIsInstance(review_dict['id'], str)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_review_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.review.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_review_name(self):
        name = "Cali"
        self.review.name = name
        self.assertEqual(self.review.name, "Cali")
        self.assertIsInstance(self.review.name, str)
