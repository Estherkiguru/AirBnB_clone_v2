#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """
        Get a list of City instances with
        state_id equals to the current State.id.
        """
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
