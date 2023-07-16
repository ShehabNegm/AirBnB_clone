#!/usr/bin/python3
"""test file using unittesting for filestorage.py"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """class for testing FileStorage class"""

    def test_storage_all(self):
        """test filestorage all method"""

        file_stor = FileStorage()
        r_dict = file_stor.all()
        self.assertIsInstance(file_stor, FileStorage)
        self.assertIsInstance(r_dict, dict)

    def test_storage_new_save(self):
        """test filestorage new method"""

        new_storage = FileStorage()
        user = User()
        new_storage.new(user)
        new_storage.save()
        new_dict = new_storage.all()
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(new_dict[key])

    def test_storage_reload(self):
        """test reload method of filestorage"""

        r_storage = FileStorage()
        r_user = User()
        r_storage.new(r_user)
        r_storage.save()
        r_storage.reload()
        rr_dict = r_storage.all()
        key = r_user.__class__.__name__ + "." + str(r_user.id)
        self.assertIsNotNone(rr_dict[key])
