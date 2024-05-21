#!/usr/bin/python3
# This script has class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

import json
import os
from models.base_model import BaseModel


class FileStorage:
    # private attributes
    __file_path = "file.json"  # path to the json file
    __objects = {}  # empty dictionary but will store all objects

    # public instance methods
    @staticmethod
    def all():
        """returns the dictionary __objects"""
        return FileStorage.__objects

    @staticmethod
    def new(obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    @staticmethod
    def save():
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    @staticmethod
    def reload():
        """Deserializes the JSON file to __objects if it exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    if cls_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**obj_data)
