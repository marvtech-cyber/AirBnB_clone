#!/usr/bin/python3
"""
This module contains the subclass: Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class is a subclass of BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
