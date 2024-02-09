#!/usr/bin/python3
"""
Testing FileStorage module cases
"""
import json
import models
import pep8
import contextlib
import os
import unittest

# Importing necessary classes from modules
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Testing case class for FileStorage module.
    """
    def test_pep8_FileStorage(self):
        """
        Testing PEP8 compliance for FileStorage module.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def cleanUp(self):
        """
        Clears the testing environment by cleaning up objects and files
        """

        # Delete instances
        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        # Remove file.json if it exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_empty(self):
        """
        Checks if the storage is not empty
        """

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_types(self):
        """
        Verify the type of data stored in the storage
        """

        self.assertEqual(dict, type(self.storage.all()))
    
    def test_add_user_to_storage(self):
        """Test the addition of a new user"""
        objects = self.storage.all()
        self.u1.id = 1345
        self.u1.name = "Irene"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(objects[key])
    
    def test_file_contains_data(self):
        """
        Check if the 'file.json' contains data after Storage Engine operations.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_documentation(self):
        """
        Verify the presence and correctness of docstrings for each function in the FileStorage class.
        """

        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))

    def test_storage_engine_loading(self):
        """
        Checks if the Storage engine loads data from the JSON file correctly
        """

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def setUp(self):
        """
        Set up the testing environment.
        """

        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

if __name__ == '__main__':
    unittest.main()
