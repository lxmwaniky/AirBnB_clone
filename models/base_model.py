#!/usr/bin/python3

"""
    This module defines the BaseModel class, which serves as the base class for other classes in the project.
    It contains common attributes and methods that are inherited by other classes.

    Attributes:
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last updated.
        id (str): The unique identifier for the instance.

    Methods:
        __init__(): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the BaseModel object.
        save(): Updates the public instance attribute updated_at with the current datetime.
        to_dict(): Returns a dictionary containing all keys/values of __dict__ of the instance.
"""

import uuid
import datetime


class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """
        Returns a string representation of the BaseModel object.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.

        Returns:
            dict: A dictionary containing all instance attributes.
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

