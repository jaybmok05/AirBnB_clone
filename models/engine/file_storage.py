#!/usr/bin/python3
"""
Defines file storage class that enables saving and 
retrieving objects from a file
"""

import json


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
        key = "{}.{}".format(obj.__class.__name, obj.id)
        FileStorage.__objects[key] = obj

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
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    obj = globals()[class_name](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
        

