#!/usr/bin/python3
"""Defines the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the user attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
