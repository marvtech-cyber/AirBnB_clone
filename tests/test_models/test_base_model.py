#!/usr/bin/python3
"""Test base_model module """
from models.base_model import BaseModel
import unittest
import datetime
import json
import os
from uuid import UUID


class test_basemodel(unittest.TestCase):
    """test base model module uniytests"""

    def __init__(self, *args, **kwargs):
        """initilizing attributes"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Runs befoure every tests"""
        pass

    def tearDown(self):
        """Runs after every tests"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """default test"""
        cls = self.value()
        self.assertEqual(type(cls), self.value)

    def test_kwargs(self):
        """testing kwarg input"""
        cls = self.value()
        temp = cls.to_dict()
        new = BaseModel(**temp)
        self.assertFalse(new is cls)

    def test_kwarg_int(self):
        """Testing kwarg with intiger input"""
        cls = self.value()
        temp = cls.to_dict()
        temp.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**temp)

    def test_save(self):
        """..."""
        cls = self.value()
        cls.save()
        key = self.name + "." + cls.id
        with open("file.json", "r") as fd:
            temp = json.load(fd)
            self.assertEqual(temp[key], cls.to_dict())

    def test_str(self):
        """.."""
        cls = self.value()
        str_t = '[{}] ({}) {}'.format(self.name, cls.id, cls.__dict__)
        self.assertEqual(str(cls), str_t)

    def test_kwargs_none(self):
        """..."""
        my_input = {None, None}
        with self.assertRaises(TypeError):
            new = BaseModel(**my_input)

    def test_kwargs_one(self):
        """..."""
        n = {'Name': 'Test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """..."""
        cls = self.value()
        i = cls.id
        self.assertEqual(str, type(i))

    def test_createdat(self):
        """...."""
        cls = self.value()
        i = cls.created_at
        self.assertEqual(type(i), datetime.datetime)

    def test_updatedat(self):
        """..."""
        cls = self.value()
        n = cls.updated_at
        self.assertEqual(type(n), datetime.datetime)
        temp = cls.to_dict()
        new = BaseModel(**temp)
        self.assertFalse(new.created_at == new.updated_at)
