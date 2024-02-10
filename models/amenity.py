#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity (models/amenity.py):

    Purpose: Represents an amenity.

    Attributes:
        name: string, optional - The name of the amenity.

    Usage:
        Create a new instance of Amenity with
            optional parameters to represent different amenities."""

    name = ""
