"""The base model class that parents all other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """blueprint for all other classes in the module

    Returns:
        BaseModel: an instance
    """
    id = str(uuid.uuid4()) # The unique id
    created_at = datetime.now()
    update_at = created_at
    
    def __str__(self):
        """prints a short description of the instance
        """
        print(f"[s{self.__class__}] ({self.id}) {self.__dict__}")   

    def save(self):
        """Update the 'update_at' with the current datetime"""
        self.update_at = datetime.now()
    
    def to_dict(self):
        """creates a dictionary description of the instance

        Returns:
            dict: a dictionary of instance attributes including
            the __class__ attribute
        """
        self.__dict__["__class__"] = self.__class__
        self.created_at = (self.created_at).strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.update_at = (self.update_at).strftime("%Y-%m-%dT%H:%M:%S.%f")
        
        return self.__dict__
