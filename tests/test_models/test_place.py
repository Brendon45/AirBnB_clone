#!/usr/bin/python3
"""
Module for testing place class
"""
import json
import pep8
from models.place import Place
from models.base_model import BaseModel
import unittest
import datetime

class TestPlace(unittest.TestCase):
    """
    The class method for testing place attributes
    """
    def test_doc_module(self):
        """
        Test case for module documentation
        """
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_place(self):
        """
        models/place.py complies to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Test case for constructor documentation.
        """
        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_test_place(self):
        """
        test_place.py complies to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                            "Found code style errors (and warnings).")


    def test_class(self):
        """Verify the methods of the place class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Place, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Place.city_id, str)
            self.assertIsInstance(Place.user_id, str)
            self.assertIsInstance(Place.name, str)
            self.assertIsInstance(Place.description, str)
            self.assertIsInstance(Place.number_rooms, int)
            self.assertIsInstance(Place.number_bathrooms, int)
            self.assertIsInstance(Place.max_guest, int)
            self.assertIsInstance(Place.price_by_night, int)
            self.assertIsInstance(Place.latitude, float)
            self.assertIsInstance(Place.longitude, float)
            self.assertIsInstance(Place.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
