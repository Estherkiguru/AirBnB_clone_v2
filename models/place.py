#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import (Column, String, ForeignKey, Float,
                        Integer)
from sqlalchemy.orm import relationship
from models.review import Review

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id)', nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024)
    number_rooms = Column(integer, default=0)
    number_bathrooms = Column(integer, default=0)
    max_guest = Column(integer, default=0)
    price_by_night = Column(integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            all_reviews
