#!/usr/bin/python3

"""Place Module:
Inherits from Superclass BaseModel
"""

from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """
    Place class that represents a place
    listing in the AirBnB clone application.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for renting the place.
        latitude (float): The latitude coordinate of the place's location.
        longitude (float): The longitude coordinate
        of the place's location.
        amenity_ids (List[str]): A list of IDs of
        amenities available in the place.
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []
