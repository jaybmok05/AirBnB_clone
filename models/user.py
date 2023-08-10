#!/usr/bin/python3
<<<<<<< HEAD
"""
Defining class user that inherits
from BaseMode
"""
=======
"""Defines the User class"""

>>>>>>> fc08444f70fd4f811a1afc730914547a3a9fc133
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """a class that will create
    user objects containing user
    details

    Attributes:
            email: string - empty string
            password: string - empty string
            first_name: string - empty strin
            last_name: string - empty string
=======
    """
    Class for User objects

    Attributes:
        email (str): email address of the user
        password (str): user password
        first_name (str): first name of the user creating the account
        last_name (str): last name of the user creating the account
>>>>>>> fc08444f70fd4f811a1afc730914547a3a9fc133
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """Costructor to instantiate User instances"""
        super().__init__(*args, **kwargs)
>>>>>>> fc08444f70fd4f811a1afc730914547a3a9fc133
