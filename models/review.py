#!/usr/bin/python3
"""The review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the review class/blueprint

    Args:
        BaseModel (object): the parent class
    """
    place_id = ""
    user_id = ""
    text = ""
