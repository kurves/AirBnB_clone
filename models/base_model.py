#!/usr/bin/python3

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


"""Define a class that instanitiate a new instance"""

class BaseModel:
    """base class that defines all attributes"""
    def __init__(self, *args, **kwargs):
        """instantiate class atrributes"""
        if kwargs:
            for k,v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """str definition for class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__) 
    
    def save(self):
        """updtae saved object"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """"return dict represntation"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy




