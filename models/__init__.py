#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .state import State
from .city import City
from .amenity import Amenity
from .place import Place
from .review import Review

storage = FileStorage()
storage.reload()
