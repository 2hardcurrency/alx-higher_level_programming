#!/usr/bin/python3
"""Contains a class Student that defines a student data"""


class Student:
    """Defines the class of student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Getter that gets the objects of the the dictionary"""
        return self.__dict__
