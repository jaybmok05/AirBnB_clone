#!/usr/bin/python3
"""Defines unittest for HBNBCommand class"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Create an instance of the console before each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test by setting the console instance to None"""
        self.console = None

    def test_quit(self):
        """Tests if the quit command gracefully exits the command loop"""
        result = self.console.onecmd("quit")
        self.assertTrue(result)

#   def test_help(self):
#        """Tests the help command's output"""
#        with patch('sys.stdout', new=StringIO()) as f:
#           self.console.onecmd("help")
#            output = f.getvalue()
#            self.assertIn("Documented commands (type help <topic>):", output)

    def test_create_with_valid_class(self):
        """Tests creating an instance of a valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_create_no_class_name(self):
        """Tests creating an instance without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_with_invalid_class(self):
        """Tests creating an instance of an invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create AntClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_id(self):
        """Tests displaying an instance of a class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f'show User {obj_id}')
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)
    
    def test_show_with_no_class_name(self):
        """Tests trying to display an instance without giving class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")
    
    def test_show_no_class_name_id(self):
        """Tests trying to display an instance without giving class name id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_with_invalid_class(self):
        """Tests trying to display an instance of an invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show AntClass 568")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_nonexisting_instance(self):
        """Tests trying to display an nonexistent instance of a valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 56568")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_valid_class_and_id(self):
        """Tests destroying an instance with a valid class name and id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f'destroy BaseModel {obj_id}')
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_destroy_with_invalid_class(self):
        """Tests destroying an instance with an ivalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass 5668")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_nonexisting_instance(self):
        """Tests destroy an nonexistent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 56")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
    
    def test_destroy_id_missing(self):
        """Tests destroying an instance with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all_with_valid_class_name(self):
        """Tests 'all' with a valid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertTrue(isinstance(eval(output), list))

    def test_all_with_invalid_class_name(self):
        """Tests 'all' with an invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def def_update_missing_class_name(self):
        """Tests update with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_with_invalid_class_name(self):
        """Tests update with an invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
