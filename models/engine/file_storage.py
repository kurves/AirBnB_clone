


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

    def reload(self):
        """Deserialize the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name, obj_id = k.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**v)
                    self.__objects[k] = obj


