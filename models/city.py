#!/usr/bin/python3
"""Blueprint for the city objects"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city object

    Args:
        BaseModel (object): the parent class
    """
    state_id = ""
    name = ""
