#!/usr/bin/python3
"""User inherits from the BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Model with more attributes

    Args:
        BaseModel (object): the parent class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
