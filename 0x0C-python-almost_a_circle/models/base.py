#!/usr/bin/python3
""" Defines a module for Base Class. """
from json import dumps, loads
import csv


class Base:
    """ Base Model
    This represents the base model for all classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the Json serialization of a list of a dictionary. """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Unjsonifies a dictionary."""
        if json_string is None or json_string == []:
            return []
        return loads(json_string)
