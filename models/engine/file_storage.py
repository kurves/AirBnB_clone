


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
        obj_dict = {k: obj.to_dict() for k, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)


