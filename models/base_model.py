#!/usr/bin/python3
"""
Attributes/Methods for BaseClass
- Public instance attributes:
    - id
    - created_at -  datetime - assign with the current datetime
    - updated_at -  datetime - assign with the current datetime
- Public instance methods
    - save(self)
    - to_dict(self)
"""


import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel class serving as the foundation for other models"""
    def __init__(self, *args, **kwargs):
        """Class constructor for the BaseModel class."""
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''string of BaseModel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)
