#!/usr/bin/python3
"""Contains class of student dictionary"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in self.__dict__:
                if key in attrs:
                    new_dict[key] = self.__dict__[key]
            return new_dict
