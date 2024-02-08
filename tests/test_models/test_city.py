#!/usr/bin/python3
"""
Test cases for the city class
"""
import json
import datetime
from models.city import City
from models.base_model import BaseModel
import pep8
import unittest

class TestCity(unittest.TestCase):
    """
    Test for the city class attribute
    """
    def test_doc_module(self):
        """Test case for module documentation."""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """
        models/city.py complies to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")
    
    def test_doc_constructor(self):
        """
        Test case for constructor documentation.
        """
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Verify the attributes of city class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)

    def test_pep8_conformance_test_city(self):
        """tests/test_models/test_city.py complies to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                            "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
