#!/usr/bin/python3
'''Test cases for the user class'''
import json
import datetime
import unittest
import pep8

from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the user class
    Test cases cover:
        - Email
        - Username
        - Password
        - Lastname
    """
    def test_doc_module(self):
        """Test case for module documentation."""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Models/user.py complies to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Test case for constructor documentation."""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_test_base_model(self):
        """tests/test_models/test_user.py complies to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                            "Found code style errors (and warnings).")
    def test_class(self):
        """
        Tests for different attributes
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)

if __name__ == '__main__':
    unittest.main()
