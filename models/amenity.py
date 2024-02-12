#!/usr/bin/python3
"""The amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """blueprints for the amenity objects

    Args:
        BaseModel (object): parent class
    """
    name = ""
