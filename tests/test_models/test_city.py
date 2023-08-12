#!/usr/bin/python3
"""Defines Unittest cases for City class"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_city_instance(self):
        """Tests City instance creation and attributes"""

        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_city_attributes(self):
        """Tests City attributes"""

        city = City()
        city.state_id = "23568"
        city.name = "Cleveland"
        self.assertEqual(city.state_id, "23568")
        self.assertEqual(city.name, "Cleveland")


if __name__ == "__main__":
    unittest.main()
