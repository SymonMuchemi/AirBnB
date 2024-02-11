#!/usr/bin/python3
"""Tests for the base model class"""
from models.base_model import BaseModel
from datetime import datetime
import unittest

form = '%Y-%m-%dT%H:%M:%S.%f'


class TestBaseModel(unittest.TestCase):
    """Test the BaseClass"""

    def test_initilization_with_arguments(self):
        time_now = datetime.now()
        test_model1 = BaseModel(id=10001, created_at=time_now)
        # Test if the id is set
        self.assertEqual(test_model1.id, 10001)
        # Test if the created_at is set
        self.assertEqual(test_model1.created_at, time_now)
        # Test if the updated_at is set to equal the created_at
        self.assertEqual(test_model1.update_at, test_model1.update_at)

    def test_init_with_no_args(self):
        """Test initialization with no arguments"""
        model = BaseModel()

        # check if model has all attributes
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.update_at)

        # check the types of the attributes of the instance
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, str)
        self.assertIsInstance(model.update_at, str)

    def test_override_id(self):
        """Check if the id can be overridden """
        model = BaseModel()
        prev_id = model.id

        model.id = "12345"
        self.assertNotEqual(model.id, prev_id)

    def test_override_created_at(self):
        """check if the created_at attribute can be overridden"""
        model = BaseModel()
        prev_created_at = model.created_at

        model.created_at = "2024-10-23"
        self.assertNotEqual(model.created_at, prev_created_at)

    def test_save_method(self):
        """check if save() updates the update_at attribute"""
        # check id update_at attribute is different from created_at
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.update_at)

    def test_to_dict(self):
        """check if to_dict() returns a dictionary object"""
        model = BaseModel(id="212323")
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)

    def test_str(self):
        """Checks if the __str__ method returns appropriate string rep"""
        model = BaseModel()
        model_dict = model.to_dict()
        model_class = model.__class__.__name__
        model_id = model.id

        model_rep = f"[{model_class}] ({model.id}) {model_dict}"

        self.assertAlmostEqual(model_rep, str(model))

    def test_time_format(self):
        """"check if time is in string format"""
        # Create a BaseModel instance
        model = BaseModel()

        # Check if created_at is a datetime object
        self.assertIsInstance(model.created_at, str)

        # Check if update_at is a datetime object
        self.assertIsInstance(model.update_at, str)

    def test_datetime_iso_format(self):
        """check if created_at and update_at are formatted in ISO format"""
        # Create a BaseModel instance
        model = BaseModel()

        self.assertTrue(datetime.strptime(model.created_at, form))

        # Check if update_at is in the expected format
        self.assertTrue(datetime.strptime(model.update_at, form))
