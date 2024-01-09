#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """A stydent class"""
    def __init__(self, first_name, last_name, age):
        """
        Instantiates a student instance

        Args:
            first_name: (str) first name
            last_name: (str) last name
            age: (int) age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description with simple data structure"""
        data = {}

        for attr in self.__dict__:
            value = getattr(self, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                data[attr] = value
        return data
