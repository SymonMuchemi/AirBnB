#!/usr/bin/python3
"""The base model class that parents all other classes"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Intializes the """
        self.id = str(uuid.uuid4()) # The unique id
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        
        if len(args) == 0:
            if len(kwargs) > 0:
                for key, val in kwargs.items():
                    if key == "id":
                        self.id = val
                    if key == "created_at":
                        self.created_at = str(val)
                    if key == "updated_at":
                        self.update_at = str(val)
        
    def save(self):
        """Update the 'update_at' with the current datetime"""
        self.update_at = datetime.now()
    
    def to_dict(self):
        """creates a dictionary description of the instance

        Returns:
            dict: a dictionary of instance attributes including
            the __class__ attribute
        """
        self.created_at = (self.created_at).strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.update_at = (self.update_at).strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__["__class__"] = self.__class__
        
        return self.__dict__

    def __str__(self):
        """prints a short description of the instance
        """
        return f"[s{self.__class__}] ({self.id}) {self.__dict__}"
