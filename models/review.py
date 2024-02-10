#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """Review (models/review.py):

    Purpose: Represents a review for a place.

    Attributes:
        place_id: string, optional - The ID of the place being reviewed.
        user_id: string, optional - The ID of the user who wrote the review.
        text: string, optional - The content of the review.

    Usage:
        Create a new instance of Review with
            optional parameters to represent different reviews."""

    place_id = ""
    user_id = ""
    text = ""
