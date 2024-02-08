#!/usr/bin/python3
"""
Module for testing the review class
"""
import json
import datetime
from models.review import Review
from models.base_model import BaseModel
import pep8
import unittest

class TestReview(unittest.TestCase):
    """
    Testing the review class
    """
    def test_doc_module(self):
        """
        Test case for module documentation.
        """
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)
    
    def test_pep8_conformance_review(self):
        """
        models/review.py complies to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")
    
    def test_doc_constructor(self):
        """
        Test case for constructor documentation.
        """
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Verify the methods of the review class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                            "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
    
