#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class for creating and managing instances.

    Attributes:
        TIME_FORMAT (str): The format string for time representation.

    Methods:
        __init__(*args, **kwargs): Initializes a new instance of BaseModel.
        __str__(): Returns a string representation of the instance.
        save(): Updates the updated_at attribute and saves the instance.
        to_dict(): Returns a dictionary of instance attributes.
    """

    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.

        Args:
            *args: Will not be used.
            **kwargs: A dictionary of key-value arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, self.TIME_FORMAT)
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self) -> dict:
        """Return a dictionary of instance attributes."""
        excluded = ['name', 'my_number']
        result = {k: v for k, v in self.__dict__.items() if k not in excluded}
        result['__class__'] = self.__class__.__name__

        for k, v in result.items():
            if isinstance(v, datetime):
                result[k] = v.isoformat()

        return result
