#!/usr/bin/python3
"""Defines the base class for AirBnB_clone project"""

import uuid
from datetime import datetime

import models


class BaseModel:
    """Manage attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Instatiate a new object"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            # models.storage.new(self)
    def __str__(self):
        """String representation of the base model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save/update the public attribute `updated_at` with current time.
        """
        self.updated_at = datetime.now()
        # models.storage.save()

    def to_dict(self):
        """Serializes object and return its dictionary"""
        D = self.__dict__.copy()
        D["created_at"] = self.created_at.isoformat()
        D["updated_at"] = self.updated_at.isoformat()
        D["__class__"] = self.__class__.__name__
        return D
