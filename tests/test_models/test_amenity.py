#!/usr/bin/python3
"""
Test case for amenity class
"""
import json
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
import unittest


class TestAmenity(unittest.TestCase):
    """
    Tests for the amenity class methods
    """
    def test_doc_module(self):
        """
        Test case for module documentation.
        """
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """
        models/amenity.py complies to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Test case for constructor documentation.
        """
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Verify the methods of the amenity class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)

    def test_pep8_conformance_test_amenity(self):
        """test_state.py complies to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
