#!/usr/bin/python3
"""Module that defines class State"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This class defines class State"""

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':

        name = column(string(128), nullable=FALSE)
        cities = relationship(
                'City', back_populates='state',
                cascade='all, delete, delete-orphan')

    else:
        name = ""

        @proparty
        def cities(self):
            """ 
            return the list of City objects from
            storage linked to the current State
            """

            cities_objs = []
            cities_dict = models.storage.all(models.City)

            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities_objs.append(value)

            return cities_objs
