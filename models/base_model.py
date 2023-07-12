#!/usr/bin/python3
# base_model.py
"""define the base_model class"""
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class"""

    def __init__(self):
        """class initialization"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """print representation of the class"""

        return ("[" + str(self.__class__.__name__) + "] (" + str(self.id)
                + ") " + str(self.__dict__))

    def save(self):
        """update updated_at with current time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary containing all keys/values of the class"""

        self.created_at = str(self.created_at)
        self.updated_at = str(self.updated_at)
        self.__dict__["__class__"] = str(self.__class__.__name__)
        return self.__dict__
