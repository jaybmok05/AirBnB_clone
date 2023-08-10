#!/usr/bin/python3
"""
Defining place class object that inherits
from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class for place object

    Attributes:
        name(string): the name of the state
        city_id(string): unique id of the city
        user_id(string): unique id for the user
        description(string): place description
        number_rooms(string): number of rooms
        number_bathrooms(string): bathroms numbers in a room
        max_guest(int): the number of people that can be
        accomodated
        price_by_night(int): price per room per night
        latitude(float): latitude of the place
        longitude(float): longitude of the place
        amenity_ids(list): list of amenties
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
