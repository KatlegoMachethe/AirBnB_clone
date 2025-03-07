#!/usr/bin/python3
"""
Module: base_model
Contains the "BaseModel" class that defines all
common attributes/methods for other classe.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the public attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dataTime = "%Y-%m-%dT %H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], dataTime)
                if key != "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """
        Prints something in special format
        """
        nameClass = self.__class__.__name__
        return ("[{}] ({}) {}".format(nameClass, self.id, self.__dict__))

    def save(self):
        """
        Mothod for updating public attr and saves them
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionery
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        formatTime = "%Y-%m-%dT %H:%M:%S.%f"
        new_dict["created_at"] = self.created_at.strftime(formatTime)
        new_dict["updated_at"] = self.updated_at.strftime(formatTime)
        return new_dict
