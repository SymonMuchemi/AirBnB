#!/usr/bin/python3
"""The base model class that parents all other classes"""
import uuid
from datetime import datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """the blueprint for model classes
    """
    def __init__(self, *args, **kwargs):
        """The class instance creator"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            # set attributes from key-worded arguments
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        val, DATE_FORMAT
                    )
                elif key == "id":
                    self.__dict__[key] = str(val)
                else:
                    self.__dict__[key] = val

    def __str__(self):
        """Return a formal representation of the BaseModel obj"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates updated_at to the current time
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """returns a dictionary description of the instance

        Returns:
            dict: the json ready form of the class instance
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        
        return dict_obj
