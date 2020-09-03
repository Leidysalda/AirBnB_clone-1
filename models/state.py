#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """property that returs a list of city instances"""
            citylist = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    citylist.append(city)
            return citylist
