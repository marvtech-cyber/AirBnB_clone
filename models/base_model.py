#!/usr/bin/python3
"""Defining base model claiss"""
import uuid
from datetime import datetime


class BaseModel:
    """initilixing base model."""
    def __init__(self, *args, **kwargs):
        """Base model instance initilizition."""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """saves file in to file.json file and update update time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Convert an instance in to modified dictionary format"""
        dictionary = {}
        dictionary.update(self.__dict__)

        dictionary.update({"__class__": type(self).__name__})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        return ("[{}] ({}) {}".
                format(type(self).__name__, self.id, self.__dict__))
