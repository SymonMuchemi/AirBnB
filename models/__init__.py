#!/usr/bin/python3
"""instantiate the file storage class and calls the reload method"""
from models.engine.file_storage import FileSorage


storage = FileSorage()
storage.reload()
