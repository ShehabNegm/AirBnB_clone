#!/usr/bin/python3
"""Defines User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
