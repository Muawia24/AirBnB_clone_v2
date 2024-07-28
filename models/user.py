#!/usr/bin/python3
"""This Module defines User Class
    """


from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
import os

class User(BaseModel, Base):
    """This Class defines User Class which has the following public class
attributes
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """

    __tablename__ = 'users'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)

        places = relationship(
                'Place', back_populates='user',
                cascade='all, delete, delete-orphan')
        reviews = relationship(
                'Review', back_populates='user',
                cascade='all, delete, delete-orphan')

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
