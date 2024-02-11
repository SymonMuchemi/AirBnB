#!/usr/bin/python3
import json

from models.engine.file_storage import FileStorage
from unittest import TestCase
from models.base_model import BaseModel


class TestFileSorage(TestCase):
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
        self.fail()

    def test_save(self):
        self.fail()

    def test_reload(self):
        self.fail()
