#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base class for all
other classes in this project.
"""
from uuid import uuid.uuid4
from datetime import datetime
import models

class BaseModel:
    """
    This class defines the BaseModel object,
    which serves as the base class for all other classes
    """
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel object
        """
        if kwargs:
            for key, value in kwargs.items():
                