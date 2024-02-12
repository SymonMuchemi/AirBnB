#!/usr/bin/python3
"""The base model class that parents all other classes"""
import uuid
from datetime import datetime

dtform = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """the blueprint for model classes
    """
    def __init__(self, *args, **kwargs):
        """initializing the base mode
        """
        self.id = str(uuid.uuid4())  # The unique id
        self.created_at = datetime.now()
        self.update_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        # Check if the instance is new and not from a dictionary representation
        if len(kwargs) == 0:
            from . import storage
            storage.new(self)

    def save(self):
        """Update the 'update_at' with the current datetime"""
        self.update_at = datetime.now()
        from . import storage
        storage.save()

    def to_dict(self):
        """creates a dictionary description of the instance

        Returns:
            dict: a dictionary of instance attributes including
            the __class__ attribute
        """
        object_dict = self.__dict__.copy()
        object_dict.update({'__class__': self.__class__.__name__})
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.update_at.isoformat()
        
        return object_dict

    def __str__(self):
        """prints a short description of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
