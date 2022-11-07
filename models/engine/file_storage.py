#!/usr/bin/python3
"""...."""
import json


class FileStorage:
    """..."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """..."""
        FileStorage.__objects.update({type(obj).__name__ + "." + obj.id: obj})

    def save(self):
        """..."""
        from models.base_model import BaseModel
        from models.user import User
        with open(FileStorage.__file_path, 'w') as fd:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, values in temp.items():
                temp[key] = values.to_dict()
            json.dump(temp, fd)

    def reload(self):
        """...."""
        from models.base_model import BaseModel
        from models.user import User
        classes = {
                    'BaseModel': BaseModel,
                    'User': User
                    }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as fd:
                temp = json.load(fd)
                for key, values in temp.items():
                    self.all()[key] = classes[values['__class__']](**values)
        except FileNotFoundError:
            pass
