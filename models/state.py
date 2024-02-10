#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """State (models/state.py):

    Purpose: Represents a state.

    Attributes:
        name: string, optional - The name of the state.

    Usage:
        Create a new instance of State with 
            optional parameters to represent different states."""

    name = ""
