#!/usr/bin/python3
"""
Defining amenity class object that inherits
from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class for amenity object

    Attributes:
        name(string): the name of the state 
    """
    name = ""
