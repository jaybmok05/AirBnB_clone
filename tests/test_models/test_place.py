#!/usr/bin/python3
"""Defines Unittest cases for Place class"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_place_instance(self):
        """Tests Place instance creation and attributes"""

        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_place_attributes(self):
        """Tests Place attributes"""

        place = Place()
        place.city_id = "2356878"
        place.name = "Sawmill Creek"
        place.user_id = "68579"
        place.description = "Facing mountains"
        place.amenity_ids = ["Air Con", "Balcony", "Wi-Fi"]
        place.number_rooms = 6
        place.number_bathrooms = 2
        place.max_guest = 4
        place.price_by_night = 1200
        place.latitude = 100.5
        place.longitude = 36.4
        self.assertEqual(place.city_id, "2356878")
        self.assertEqual(place.name, "Sawmill Creek")
        self.assertEqual(place.user_id, "68579")
        self.assertEqual(place.description, "Facing mountains")
        self.assertEqual(place.amenity_ids, ["Air Con", "Balcony", "Wi-Fi"])
        self.assertEqual(place.number_rooms, 6)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 1200)
        self.assertEqual(place.latitude, 100.5)
        self.assertEqual(place.longitude, 36.4)


if __name__ == "__main__":
    unittest.main()
