#!/usr/bin/python3
"""The base model class that parents all other classes"""
import uuid
from datetime import datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """the blueprint for model classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at
        
    def __str__(self):
        """Return a formal representation of the BaseModel obj"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates updated_at to the current time
        """
        self.update_at = datetime.now()
        
    def to_dict(self):
        """returns a dictionary description of the instance

        Returns:
            dict: the json ready form of the class instance
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.update_at.isoformat()
        
        return dict_obj
