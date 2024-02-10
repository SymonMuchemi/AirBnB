#!/usr/bin/python3
"""The base model class that parents all other classes"""
import uuid
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """the blueprint for model classes
    """
    def __init__(self, *args, **kwargs):
        """initializing the base mode
        """
        self.id = str(uuid.uuid4()) # The unique id
        self.created_at = datetime.now()
        self.update_at = self.created_at
        
        if len(args) == 0:
            if len(kwargs) > 0:
                for key, val in kwargs.items():
                    if key == "id":
                        self.id = val
                    if key == "created_at":
                        if isinstance(val, str):
                            self.created_at = datetime.strptime(val, date_format)
                        self.created_at = val
                    if key == "updated_at":
                        if isinstance(val, str):
                            self.created_at = datetime.strptime(val, date_format)
                        self.update_at = val
        # Check if the instance is new and not from a dictionary representation
        if len(args) == 0 and len(kwargs) == 0:
            from . import storage
            storage.new(self)
        
    def save(self):
        """Update the 'update_at' with the current datetime"""
        self.update_at = str(datetime.now())
        from . import storage
        storage.save()
    
    def to_dict(self):
        """creates a dictionary description of the instance

        Returns:
            dict: a dictionary of instance attributes including
            the __class__ attribute
        """
        self.created_at = (self.created_at).strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.update_at = (self.update_at).strftime("%Y-%m-%dT%H:%M:%S.%f")
        
        # convert time to str format for serialization
        
        self.created_at = str(self.created_at)
        self.update_at = str(self.update_at)
        self.__dict__["__class__"] = self.__class__.__name__
        
        return self.__dict__

    def __str__(self):
        """prints a short description of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
