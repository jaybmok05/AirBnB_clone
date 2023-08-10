#!/usr/bin/python3
"""
Defining state class object that inherits
from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class for states object

    Attributes:
        name(string): the name of the state
    """
    name = ""
