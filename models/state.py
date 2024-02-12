#!/usr/bin/python3
"""The state blueprint"""
from models.base_model import BaseModel


class State(BaseModel):
    """Blueprint for the state objects

    Args:
        BaseModel (object): the parent class
    """
    name = ""
