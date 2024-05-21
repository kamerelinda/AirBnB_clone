#!/usr/bin/python3
# test cases for the console.py:

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models import storage


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment"""
        del self.console

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check if the ID is printed

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            # Check if the output contains BaseModel
            self.assertTrue("BaseModel" in output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("destroy BaseModel")
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            # Check if no instance is found after destroy
            self.assertTrue("** no instance found **" in output)

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all")
            output = f.getvalue().strip()
            # Check if BaseModel instance is present in all output
            self.assertTrue("BaseModel" in output)

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            # Check if count is 1 after creating an instance
            self.assertEqual(output, "1")

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("update BaseModel 1234-1234-1234 "
                                "email 'test@example.com'")
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            # Check if email is updated
            self.assertTrue("'email': 'test@example.com'" in output)

    def test_all_with_class_name(self):
        """Test all command with class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create State")
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)
            self.assertFalse("User" in output)
            self.assertFalse("State" in output)

    def test_update_with_dictionary(self):
        """Test update command with dictionary representation"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("update BaseModel 1234-1234-1234 "
                                "{'email': 'test@example.com', "
                                "'name': 'test'}")
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertTrue("'email': 'test@example.com'" in output)
            self.assertTrue("'name': 'test'" in output)

    def test_show_invalid_id(self):
        """Test show command with invalid ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Assuming 1234 is an invalid ID
            self.console.onecmd("show BaseModel 1234")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Assuming 1234 is an invalid ID
            self.console.onecmd("destroy BaseModel 1234")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)


if __name__ == '__main__':
    unittest.main()
