#!/usr/bin/python3
"""
Module for the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class of Amenities
    Public class attributes:
        - name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance."""
        super().__init__(*args, **kwargs)
