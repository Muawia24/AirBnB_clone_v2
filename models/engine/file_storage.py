#!/usr/bin/python3
"""File storage Module that take care of the object management"""

import importlib
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    File storage is a class that allows you to
        - Serialise instances
        - Desirialise instances
        - Save Objects in a JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return dictionary of __objects"""

        if cls is not None:
            new_dict = {}
        for key, value in self.__objects.items():
            if cls == value.__class__ or cls == value.__class__.__name__:
                new_dict[key] = value
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the json file"""
        serialized_objs = {}
        for key, value in self.all().items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(serialized_objs, json_f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """ deserializing the JSON file to objects """
        self.reload()
