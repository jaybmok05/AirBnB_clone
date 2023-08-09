#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Defines unittests for User class"""

    def test_attributes(self):
        """Test User attrubutes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_inheritence(self):
        """Test inheritence"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes_default_values(self):
        """Test User attributes default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        user = User()
        user_dict = user.to_dict()
        self.assertTrue("__class__" in user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertTrue("id" in user_dict)
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)

if __name__ == "__main__":
    unittest.main()
