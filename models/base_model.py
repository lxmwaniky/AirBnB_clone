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
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, self.DATE_FORMAT)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        