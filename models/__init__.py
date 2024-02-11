#!/usr/bin/python3
"""instantiate the file storage class and calls the reload method"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
