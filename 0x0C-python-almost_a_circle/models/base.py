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
