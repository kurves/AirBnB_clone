#!/usr/bin/python3

import uuid
from datetime import datetime


"""Define a class that instanitiate a new instance"""

class BaseModel:
    """base class that defines all attributes"""
    def __init__(self, *args, **kwargs):
        """instantiate class atrributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """updtae saved object"""
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """"return dict represntation"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_copy['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict_copy
    
    def __str__(self):
        """str definition for class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__))
