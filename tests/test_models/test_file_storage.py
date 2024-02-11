#!/usr/bin/python3
import json, os

from models.engine.file_storage import FileStorage
from unittest import TestCase
from models.base_model import BaseModel


class TestFileSorage(TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file_path = "test_file.json"
        with open(self.temp_file_path, "w") as f:
            json.dump({"test_id": {"attr1": "value1", "attr2": "value2"}}, f)

    def tearDown(self):
        # Remove the temporary file after testing
        os.remove(self.temp_file_path)
        
    def test_all(self):
        """Test to see if all objects in the __objects are returned as expected"""
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

        test_object = BaseModel()
        test_object.save()

        # check if file.json contains the new object created
        obj_class_name = test_object.__class__.__name__
        obj_id = test_object.id
        key_in_file = f"{obj_class_name}.{obj_id}"

        # read file.json and check if the key is available
        with open("./file.json", 'r', encoding='utf-8') as file:
            objects_stored = json.load(file)
            self.assertIn(key_in_file, objects_stored)

    def test_new(self):
        """checks if the new() method adds the object to the json file with the correct key"""
        storage = FileStorage()
        test_object = BaseModel()
        storage.new(test_object)
        storage.save()
        obj_class_name = test_object.__class__.__name__
        obj_id = test_object.id
        key_in_file = f"{obj_class_name}.{obj_id}"
        
        with open("./file.json", 'r', encoding='utf-8') as file:
            objects_stored = json.load(file)
            self.assertIn(key_in_file, objects_stored)

    def test_save(self):
        """Checks if the save method serializes approriately"""
        storage = FileStorage()
        test_object1 = BaseModel()
        test_object2 = BaseModel()
        test_object3 = BaseModel()
        storage.new(test_object1)
        storage.new(test_object2)
        storage.new(test_object3)
        storage.save()

        # checks if all objects are in the JSON file        
        with open("./file.json", 'r', encoding='utf-8') as file:
            objects_stored = json.load(file)
            all_objects = storage.all()
            
            # Check if each object is present in objects_stored
            for obj_id, obj in all_objects.items():
                self.assertIn(obj_id, objects_stored)
                self.assertEqual(obj, objects_stored[obj_id])

    def test_reload_existing_file(self):
        """Test reloading from an existing JSON file"""
        storage = FileStorage()
        storage._FileStorage__file_path = self.temp_file_path  # Set the file path to the temporary file
        storage.reload()

        # Check if the objects were loaded correctly
        expected_objects = {"test_id": {"attr1": "value1", "attr2": "value2"}}
        self.assertEqual(storage._FileStorage__objects, expected_objects)

    def test_reload_empty_file(self):
        """Test reloading from an empty JSON file"""
        # Create an empty JSON file
        with open(self.temp_file_path, "w") as f:
            f.write("")

        storage = FileStorage()
        storage._FileStorage__file_path = self.temp_file_path  # Set the file path to the temporary file
        storage.reload()

        # Check if the objects were reloaded as an empty dictionary
        self.assertEqual(storage._FileStorage__objects, {})

    def test_reload_nonexistent_file(self):
        """Test reloading from a non-existent JSON file"""
        # Use a non-existent file path
        non_existent_file_path = "non_existent_file.json"

        storage = FileStorage()
        storage._FileStorage__file_path = non_existent_file_path  # Set the file path to the non-existent file
        storage.reload()

        # Check if the objects were reloaded as an empty dictionary
        self.assertEqual(storage._FileStorage__objects, {})
