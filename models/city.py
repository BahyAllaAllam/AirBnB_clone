#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """City (models/city.py):

    Purpose: Represents a city.

    Attributes:
        state_id: string, optional - The ID of the state the city belongs to.
        name: string, optional - The name of the city.

    Usage:
        Create a new instance of City with
            optional parameters to represent different cities."""

    state_id = ""
    name = ""
