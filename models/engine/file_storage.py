#!/usr/bin/python3
# file_storage.py
"""define FileStorage class"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        for k in self.__objects.keys():
            self.__objects[k] = self.__objects[k].to_dict()
        filename = self.__file_path
        with open(filename, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        filename = FileStorage.__file_path
        if not os.path.isfile(filename):
            pass

        else:
            with open(filename, 'r') as f:
                r_dict = json.load(f)
                for v in r_dict.values():
                    del v["__class__"]
                    self.new(BaseModel(**v))
