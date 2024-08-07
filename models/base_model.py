#!/usr/bin/python3
"""
    Module representing the Base class of
    all the classes
"""


from datetime import datetime
import models
from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()


class BaseModel:
    """
    BaseModel is a base class for all the future classes

    Args:
        id(string): unique identifier for each instance
        created_at(datetime): time when the instance is created
        updated_at(datetime): time when the instance is updated
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwrags):
        """Init function of the BaseModel class"""
        str_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwrags and len(kwrags) > 1:
            for key, value in kwrags.items():
                if (key != "__class__"):
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,
                                datetime.strptime(value, str_format))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update the public instance attribute updated_at
            with the current time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """change the object to a disctionary"""
        base_dict = {"__class__": self.__class__.__name__}

        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                base_dict[key] = value.isoformat()
            else:
                base_dict[key] = value
        return base_dict

    def delete(self):
        """ Delete current instance of storage """
        models.storage.delete(self)

    def __str__(self):
        """String representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)
