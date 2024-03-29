#!/usr/bin/python3
"""
Module to test state class
"""
import json
import pep8
import datetime
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """
    Test class method for State class
    """
    def test_doc_module(self):
        """Test case for module documentation."""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_state(self):
        """models/state.py complies to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Test case for constructor documentation."""
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Verify mothod class state"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)

    def test_pep8_conformance_test_state(self):
        """ tests/test_models/test_state.py complies to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
