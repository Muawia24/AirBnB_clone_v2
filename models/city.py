#!/usr/bin/python3
"""Module that defines class City"""

from models.base_model import BaseModel
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class City(BaseModel):
    """This class defines class City"""

    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(states.id), nullable=False)
        state = relationship('State', back_populates='cities')
    else:
        name = ""
        state_id = ""
