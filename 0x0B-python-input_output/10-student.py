#!/usr/bin/python3
"""Defines a class Student."""


class Student:
        """student class."""
        def __init__(self, first_name, last_name, age):
            """Initialize a new Student."""
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

        def to_json(self, attrs=None):
            """Get a dictionary representation of the Student.
            If attrs is a list of strings, represents only those attributes
            included in the list.
            """
            try:
                for attr in attrs:
                    if type(attr) is not str:
                            return self.__dict__
            except Exception:
                return self.__dict__
            my_dict = dict()
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict
