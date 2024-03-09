#!/usr/bin/python3

from models.base_model import BaseModel

"""class basemodelencoder"""

class BaseModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return obj.to_dict()
        return super().default(obj)

import json
import os

""""class file storage"""

class FileStorage:
    """class that serislisez and desiarializes"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return the objects."""
        return self.__objects

    def new(self, obj):
        """objects the obj with key <obj class name>.id."""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    
    def save(self):
        """Serialize to the JSON file."""
        serialized_objects = {}
        for k, obj in self.__objects.items():
            serialized_objects[k] = obj.to_dict()
        try:
            with open(self.__file_path, 'w') as f:
                json.dump(serialized_objects, f, cls=BaseModelEncoder)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    class_name, obj_id = k.split('.')
                    module = __import__('models.' + class_name.lower(), fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
