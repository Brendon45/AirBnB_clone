#!/usr/bin/python3
"""
Creating a unique File Storage instance for hbnb application
"""
from models.engine.file_storage import FileStorage


# Initialize a single instance of FileStorage
storage = FileStorage()
storage.reload
