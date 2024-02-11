#!/usr/bin/python3

"""File Storage class
for serialization into a JSON file and
deserialization of JSON file
into an instances.
"""


import json
from os import path
from models import *

class FileStorage:
    """
    This class represents a file storage system for
    serializing and deserializing objects to/from a JSON file.

    Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all
    objects by <class name>.id
    """

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

        __file_path = "file.json"
        __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                    for key, value in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        cls = self.CLASSES[class_name]
                        obj = cls(**value)
                        self.__objects[key] = obj
