#!/usr/bin/python3
"""Class inheriting from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes
        - state_id: string - empty string: it will be the State.id
        - name: string - empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
