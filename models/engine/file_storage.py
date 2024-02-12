#!/usr/bin/python3
"""handles object storage to JSON file as
well as deserialization
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes 
    JSON files to instances"""
    def __init__(self):
        """creates instances of the file storage class"""
        # path to the JSON file
        self.__file_path = 'file.json'
        # dictionary to store all objects by <classname>.id
        self.__objects = {}
        
    def all(self):
        """returns all objects saved

        Returns:
            dict: the dictionary containing all objects saved
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the instance with the key:
        <obj class name>.id

        Args:
            obj (any): dictionary object
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes the objects in __objects to the JSON file"""
        obj_dict = {}
        # TODO: check on the value.to_dict() incase of failure
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects if the file exists"""
        import os.path
        # TODO: this part might cause a bug
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)()
                    class_obj.__dict__.update(value)
                    self.__objects[key] = class_obj
