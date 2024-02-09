#!/usr/bin/python3
"""
Testing the basemodel class module for every function
"""
import json
import datetime
import pep8
from time import sleep
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """
    A base class that withhold all test cases
    """
    def test_doc_module(self):
        """Test case for module documentation."""
        doc = BaseModel._doc_
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """
        models/base_model.py complies to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")
    
    def test_doc_constructor(self):
        """
        Test case for constructor documentation
        ."""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """
        Creation of the test BaseModel instance and its conversion to a dictionary
        """
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        """
        Test base types for BaseModel attributes.
        """
        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Simon"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Simon")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_datetime_model(self):
        """
        Test datetime attributes in BaseModel.
        """
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_string_representation(self):
        """
        Test the string representation of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

        expected = '[BaseModel] ({}) {}'\
                    .format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_kwargs(self):
        """
        Constructortesting keyword arguments(kwargs) as attribute values
        """
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_save_method(self):
        """
        Testing the save method of the class
        """
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r' as f:
                self.assertIn(b3.id, f.read())

    def test_pep8_conformance_test_base_model(self):
        """
        test_base_model.py complies to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(res.total_errors, 0,
                            "Found code style errors (and warnings).")

    def test_uuid(self):
        """
        Test generation of unique UUIDs
        ."""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

if __name__ == '__main__':
    unittest.main()
