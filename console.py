#!/usr/bin/python3

import cmd
from datetime import datetime

CLASSES = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}