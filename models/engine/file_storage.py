#!/usr/bin/python3
"""handles object storage to JSON file as
well as deserialization
"""
import json
from models.base_model import BaseModel


class FileStorage:
    def __init__(self):
        """the blueprint for the class
        """
        self.__file_path = "./file.json"
        self.__objects = {}
        
    def all(self):
        """retrieves the dict of all objects

        Returns:
            dict: list of objects stored
        """
        return self.__objects
    
    def new(self, obj):
        """sets in __objects obj with the key 
        <obj class name>.id
        """
        if isinstance(obj, BaseModel):
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict() 
        
    def save(self):
        """save the __object dictionary to JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except json.JSONDecodeError:
            self.__objects = {}
        except FileNotFoundError:
            pass
