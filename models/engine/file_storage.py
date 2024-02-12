#!/usr/bin/python3
"""handles object storage to JSON file as
well as deserialization
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    def __init__(self):
        """the blueprint for the class
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """retrieves the dict of all objects

        Returns:
            dict: list of objects stored
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects obj with the key
        <obj class name>.id
        """
        if isinstance(obj, BaseModel):
            obj_key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[obj_key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dictionary = {key: obj.to_dict()
                       for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for obj_data in data.values():
                    cls_name = obj_data.get("__class__")
                    if cls_name:
                        cls = self.get_class_by_name(cls_name)
                        if cls:
                            obj = cls(**obj_data)
                            self.new(obj)
        except Exception:
            pass
