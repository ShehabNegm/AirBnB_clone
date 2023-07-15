#!/usr/bin/python3
"""Defines User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class
    arrtibutes
          email (str)
          password (str)
          first_name (str)
          last_name (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
