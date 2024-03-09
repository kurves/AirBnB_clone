#!/usr/bin/python3

import json
import os

""""class file storage"""

class FileStorage:
    """class that serislisez and desiarializes"""
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self, file_path=None):
        """Initializes the FileStorage with an optional file path."""
        if file_path:
            self.__file_path = file_path

        self.reload()


    def all(self):
        """Return the objects."""
        return self.__objects

    def new(self, obj):
        """objects the obj with key <obj class name>.id."""
        k = f"{type(obj).__name__}.{obj.id}"
        self.__objects[k] = obj

    
    def save(self):
        """Serialize to the JSON file."""
        try:
            with open(self.__file_path, "w") as f:
                json.dump(self.__objects, f, default=self.encode)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
                for k, v in self.__objects.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name.lower(), fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass

    def encode(self, obj):
        """Customizes JSON serialization for BaseModel objects."""
        if isinstance(obj, BaseModel)
            return obj.to_dict()
        return obj

     def decode(self, obj):
        """Customizes JSON deserialization for BaseModel objects."""
        if "__class__" in obj and obj["__class__"] == "BaseModel":
            from models.base_model import BaseModel
            return BaseModel(**obj)
        return obj
