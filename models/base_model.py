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
    def __init__(self, *args, **kwargs):