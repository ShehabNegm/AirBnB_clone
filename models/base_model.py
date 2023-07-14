#!/usr/bin/python3
# base_model.py
"""defines the base_model class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """class initialization"""
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """print representation of the class"""

        return ("[" + str(self.__class__.__name__) + "] (" + str(self.id)
                + ") " + str(self.__dict__))

    def save(self):
        """update updated_at with current time"""

        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary containing all keys/values of the class"""

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        r_dict = self.__dict__
        r_dict["__class__"] = self.__class__.__name__
        return r_dict
