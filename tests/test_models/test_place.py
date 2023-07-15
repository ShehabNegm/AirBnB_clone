#!/usr/bin/python3
# test_place.py
"""unittesting for BaseModel subclass Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
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
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertIsInstance(place_dict['id'], str)
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_place_to_dict_keys(self):
        keys = ['id', 'updated_at', 'created_at', '__class__']
        dic_object = self.place.to_dict()
        self.assertCountEqual(keys, dic_object.keys())

    def test_place_city_id(self):
        city_id = "0369"
        self.place.city_id = city_id
        self.assertEqual(self.place.city_id, "0369")
        self.assertIsInstance(self.place.city_id, str)

    def test_place_user_id(self):
        user_id = "2468"
        self.place.user_id = user_id
        self.assertEqual(self.place.user_id, "2468")
        self.assertIsInstance(self.place.user_id, str)

    def test_place_name(self):
        name = "Santorini"
        self.place.name = name
        self.assertEqual(self.place.name, "Santorini")
        self.assertIsInstance(self.place.name, str)

    def test_place_description(self):
        description = "Lovely Island"
        self.place.description = description
        self.assertEqual(self.place.description, "Lovely Island")
        self.assertIsInstance(self.place.description, str)

    def test_place_number_rooms(self):
        number_rooms = 1
        self.place.number_rooms = number_rooms
        self.assertEqual(self.place.number_rooms, 1)
        self.assertIsInstance(self.place.number_rooms, int)

    def test_place_number_bathrooms(self):
        number_bathrooms = 2
        self.place.number_bathrooms = number_bathrooms
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_place_max_quest(self):
        max_guest = 3
        self.place.max_guest = max_guest
        self.assertEqual(self.place.max_guest, 3)
        self.assertIsInstance(self.place.max_guest, int)

    def test_place_price_by_night(self):
        price_by_night = 500
        self.price_by_night = price_by_night
        self.assertEqual(self.price_by_night, 500)
        self.assertIsInstance(self.place.price_by_night, int)

    def test_place_longitude(self):
        longitude = 44.55
        self.place.longitude = longitude
        self.assertEqual(self.place.longitude, 44.55)
        self.assertIsInstance(self.place.longitude, float)

    def test_place_latitude(self):
        latitude = 22.66
        self.place.latitude = latitude
        self.assertEqual(self.place.latitude, 22.66)
        self.assertIsInstance(self.place.latitude, float)

    def test_place_amenity_ids(self):
        amenity_ids = [45, 105, 67]
        self.place.amenity_ids = amenity_ids
        self.assertEqual(self.place.amenity_ids, [45, 105, 67])
        self.assertIsInstance(self.place.amenity_ids, list)
