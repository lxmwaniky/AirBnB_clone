#!/usr/bin/python3
"""
This module defines the User class, which represents a user in the HBNB project.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """Defines the User model."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""