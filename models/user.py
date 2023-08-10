#!/usr/bin/python3
"""
Defining class user that inherits
from BaseMode
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class for User objects

    Attributes:
        email (str): email address of the user
        password (str): user password
        first_name (str): first name of the user creating the account
        last_name (str): last name of the user creating the account
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Costructor to instantiate User instances"""
        super().__init__(*args, **kwargs)
