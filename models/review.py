#!/usr/bin/python3
"""
Defining review class object that inherits
from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class for review object

    Attributes:
        place_id(string): unique id  for the place
        user_id(string): unique for the user
        text(string): the review made by the user
    """
    place_id = ""
    user_id = ""
    text = ""
