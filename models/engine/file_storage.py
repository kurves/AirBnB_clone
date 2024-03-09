#!/usr/bin/python3

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
                json.dump(serialized_objects, f)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for k, obj_dict in serialized_objects.items():
                    class_name, obj_id = k.split('.')
                    cls = eval(class_name)
                    obj = cls(**obj_dict)
                    self.__objects[k] = obj
        except FileNotFoundError:
            pass

    def encode(self, obj):
        """Customizes JSON serialization for BaseModel objects."""
        if isinstance(obj, BaseModel):
            return obj.to_dict()
        return obj

    def decode(self, obj):
        """Customizes JSON deserialization for BaseModel objects."""
        if "__class__" in obj and obj["__class__"] == "BaseModel":
            from models.base_model import BaseModel
            return BaseModel(**obj)
        return obj
