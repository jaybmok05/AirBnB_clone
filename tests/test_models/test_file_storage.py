#!/usr/bin/python3
"""defines unit test cases for FileStorage class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test suit for the FileStorage class"""

    def setUp(self):
        """Set up a new FileStorage instance for each test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up by removing the JSON file created during testing"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_file_path_exists(self):
        """
        Test if the __file_path attribute exists in the FileStorage instance
        """
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))

    def test_objects_exists(self):
        """
        Test if the __objects attribute exists in the FileStorage instance
        """
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_all_method(self):
        """Test the all() method of FileStorage"""
        all_obj = self.storage.all()
        self.assertIsInstance(all_obj, dict)
        self.assertEqual(len(all_obj), len(self.storage._FileStorage__objects))

    def test_new_method(self):
        """Test the new() method of FileStorage"""
        base_model = BaseModel()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.storage.new(base_model)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_and_reload_methods(self):
        """Test the save and reload() methods of FileStorage"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, new_storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
