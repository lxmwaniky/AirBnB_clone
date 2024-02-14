#!/usr/bin/python3

"""
User Module: Inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    This class represents a user in the system and stores
    information such as email, password, first name, and last name.
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
