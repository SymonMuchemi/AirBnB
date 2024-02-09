#!/usr/bin/python3
"""Tests for the base model class"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Test the BaseClass"""
    def test_initilization_with_arguments(self):
        time_now = datetime.now()
        test_model1 = BaseModel(id=10001, created_at=time_now)
        # Test if the id is set
        self.assertEqual(test_model1.id, 10001)
        # Test if the created_at is set
        self.assertEqual(test_model1.created_at, str(time_now))
        # Test if the updated_at is set to equal the created_at
        self.assertEqual(test_model1.update_at, test_model1.update_at)        
