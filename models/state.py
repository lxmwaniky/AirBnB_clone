#!/usr/bin/python3

"""State Module:
Inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that represents a state in the AirBnB clone application.

    Attributes:
        name (str): The name of the state.
    """

    name: str = ""
