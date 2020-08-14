#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", cascade="all, delete")
    elif getenv('HBNB_TYPE_STORAGE') == "file":
        @property
        def cities(self):
            """property that returs a list of city instances"""
            citylist = []
            for city in storage.all(City).values():
                if self.id == city.state_id:
                    citylist.append(city)
            return citylist
