#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """Place (models/place.py):

    Purpose: Represents a place.

    Attributes:
        city_id: string, optional -
            The ID of the city the place is located in.
        user_id: string, optional - The ID of the user who owns the place.
        name: string, optional - The name of the place.
        description: string, optional - Description of the place.
        number_rooms: int, optional - Number of rooms in the place.
        number_bathrooms: int, optional - Number of bathrooms in the place.
        max_guest: int, optional -
            Maximum number of guests allowed in the place.
        price_by_night: int, optional - Price per night for the place.
        latitude: float, optional - Latitude coordinate of the place.
        longitude: float, optional - Longitude coordinate of the place.
        amenity_ids: list of strings, optional -
            List of IDs of amenities available in the place.

    Usage:
        Create a new instance of Place with
            optional parameters to represent different places."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
