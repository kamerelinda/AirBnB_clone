#!/usr/bin/python3
# This script has class User that inherits from BaseModel:

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
