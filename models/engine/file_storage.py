#!/usr/bin/python3
"""
Defines file storage class that enables saving and 
retrieving objects from a file
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    A class for serializing instances to a JSON file and 
    deserializing JSON file to instances.

    Private class attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): dictionery to store instances by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionery of all objects.

        Returns:
            dict: dictionary with all instances by <class name>.id
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets an object in the __objects dictionary.

        Args:
            obj: An instance to store.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, obj in obj_dict.items():
                    class_name = obj['__class__']
                    del obj["__class__"]
                    self.__objects[key] = globals()[class_name](**obj)
        except FileNotFoundError:
            pass
        
    def classes(self):
        """
        Returns a dictionary of classes that can be managed by the storage
        """
        return {
            "BaseModel": BaseModel,
            "User": User
        }
