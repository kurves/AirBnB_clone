#!/usr/bin/python3

import json
import os

""""class file storage"""

class FileStorage:
    """class that serislisez and desiarializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self): """Return the objects."""
        return self.__objects

    def new(self, obj):
        """objects the obj with key <obj class name>.id."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[k] = obj

    
    def save(self):
        """Serialize to the JSON file."""
        serialized_objects = {}
        for k, v in self.__objects.items():
            serialized_objects[k] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

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
