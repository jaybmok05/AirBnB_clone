#!/usr/bin/python3
"""
Defining city class object that inherits
from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class for city object

    Attributes:
        name(string): the name of the state
        state_id(string): it will be a unique id for the city
    """
    state_id = State.id
    name = ""
