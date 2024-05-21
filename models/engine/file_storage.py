#!/usr/bin/python3
# This script has class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


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
                    cls_name = obj_data['__class__']
                    if cls_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**obj_data)
                    elif cls_name == "User":
                        FileStorage.__objects[key] = User(**obj_data)
                    elif cls_name == "State":
                        FileStorage.__objects[key] = State(**obj_data)
                    elif cls_name == "City":
                        FileStorage.__objects[key] = City(**obj_data)
                    elif cls_name == "Place":
                        FileStorage.__objects[key] = Place(**obj_data)
                    elif cls_name == "Review":
                        FileStorage.__objects[key] = Review(**obj_data)
                    elif cls_name == "Amenity":
                        FileStorage.__objects[key] = Amenity(**obj_data)
