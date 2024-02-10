#!/usr/bin/python3
"""handles object storage to JSON file as
well as deserialization
"""
import json, os


class FileSorage:
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
        if type(obj) is dict:
            self.__objects[f"{obj.classname}.{obj.id}"] = obj 
        
    def save(self):
        """save the __object dictionary to JSON file
        """
        with open(self.__file_path, 'w+', encoding='utf-8') as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r', encoding='utf-8') as fp:
            return json.load(fp)
