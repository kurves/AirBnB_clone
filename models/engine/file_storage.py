#!/usr/bin/python3

import json
import os

""""class file storage"""

class FileStorage:
    """class that serislisez and desiarializes"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self, file_path=None):
        """ïnitilize file path"""
        if file_path:
            self.__file_path = file_path

        self.reload()

    def all(self):
        """Return the objects."""
        return self.__objects

    def new(self, obj):
        """objects the obj with key <obj class name>.id."""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    
    def save(self):
        """Serialize to the JSON file."""
        obj_dict = {k: obj.to_dict() for k, obj in self.__objects.items()}
        try:
            with open(self.__file_path, 'w') as f:
                json.dump(obj_dict, f)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserialize the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
            except FileNotFoundError:
                pass
