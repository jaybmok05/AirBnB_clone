#!/usr/bin/python3
"""
Defining class user that inherits
from BaseMode
"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class that will create
    user objects containing user
    details

    Attributes:
            email: string - empty string
            password: string - empty string
            first_name: string - empty strin
            last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
