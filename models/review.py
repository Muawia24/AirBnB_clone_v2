#!/usr/bin/python3
"""Module that defines class Review"""

from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import os


class Review(BaseModel, Base):
    """This class defines class Review"""

    __tablename__ = 'reviews'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship(
            'User', back_populates='reviews')  # cascade? slave
        place = relationship(
            'Place', back_populates='reviews')  # cascade? slave

    else:
        place_id = ""
        user_id = ""
        text = ""
