#!/usr/bin/python3
"""
This module defines the Review class, which represents a review in the HBNB project.
"""
from models.base_model import BaseModel

class Review(BaseModel):
        """
        This class defines the Review object, which represents a review in the HBNB project.
        """
        place_id = ""
        user_id = ""
        text = ""