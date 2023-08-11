#!/usr/bin/python3
"""Defines Unittest cases for Amenity class"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""
    
    def test_amenity_instance(self):
        """Tests Amenity instance creation and attributes"""
        
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        
    def test_amenity_attributes(self):
        """Tests Amenity attributes"""
        
        amenity = Amenity()
        amenity.name = "RoomService"
        self.assertEqual(amenity.name, "RoomService")
        
if __name__ == "__main__":
    unittest.main()
