#!/usr/bin/python3
# This script has class City that inherits from BaseModel
# and defines cities:

from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""
