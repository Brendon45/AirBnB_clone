#!/usr/bin/python3
"""State class inheriting from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class representing a geographical state."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises a State instance."""
        super().__init__(*args, **kwargs)
