#!/usr/bin/python3

import json
import os
import importlib

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
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    
    def save(self):
        """Serialize to the JSON file."""
        serialized_objects = {}
        for k, v in self.__objects.items():
            serialized_objects[k] = v.to_dict()
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
                for key, value in serialized_objects.items():
                    class_name = value.pop('__class__')
                    try:
                        module = importlib.import_module(f'models.{class_name}')
                    except ImportError:
                        print(f"Error loading module '{class_name}'")
                        continue  # Skip to the next object
                    cls = getattr(module, class_name)
                    instance = cls(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
