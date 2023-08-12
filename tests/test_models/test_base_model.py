#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test suit for the BaseModel class"""

    def setUp(self):
        """ Sets up a new BaseModel instance for each test"""
        self.base_model = BaseModel()

    def test_attributes(self):
        """
        Tests the existance of essential attributes in a BaseModes instance
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """Test if the 'id' attribute is a string"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        """Test data type of the 'created_at' attribute"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test data type of the 'updated_at' attribute"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation of a BaseModel instance"""
        desired = "[BaseModel] ({}) {}".format(self.base_model.id,
                                               self.base_model.__dict__)
        self.assertEqual(str(self.base_model), desired)


if __name__ == '__main__':
    unittest.main()
