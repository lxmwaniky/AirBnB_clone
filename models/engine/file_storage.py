#!/usr/bin/python3

"""File Storage class for serialization into a JSON file and deserialization of JSON file into instances."""

import json
from os import path
from models import *


class FileStorage:
    """This class represents a file storage system for serializing and deserializing objects to/from a JSON file."""

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # dictionary to store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    self.__objects[key] = obj_instance
