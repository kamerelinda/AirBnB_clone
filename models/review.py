#!/usr/bin/python3
# This script has class Review that inherits from BaseModel
# and defines reviews:

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
