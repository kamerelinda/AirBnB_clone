#!/usr/bin/python3
# This script has class BaseModel that defines all common attributes/methods for other classes:

import uuid
from datetime import datetime



class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()  # Set created_at to current datetime
            self.updated_at = datetime.now()  # Set updated_at initially to created_at
            from models import storage
            storage.new(self)  # add to storage

    def __str__(self):
        # [<class name>] (<self.id>) <self.__dict__>
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # updates the public instance attribute updated_at with the current datetime
        self.updated_at = datetime.now()
        from models import storage
        storage.save()  # save to storage

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
