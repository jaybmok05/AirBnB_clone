#!/usr/bin/python3
"""Defines a class of Unittest cases for the State class"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the State class"""
    
    def test_state_instance(self):
        """Tests State attributes and instance creation"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "created_at"))

    def test_state_attributes(self):
        """Tests State attributes"""
        state = State()
        state.name = "Ohio"
        self.assertEqual(state.name, "Ohio")

if __name__ == "__main__":
    unittest.main()
