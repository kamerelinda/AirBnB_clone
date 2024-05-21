#!/usr/bin/python3
# file creates a unique FileStorage instance and call its reload method:

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
