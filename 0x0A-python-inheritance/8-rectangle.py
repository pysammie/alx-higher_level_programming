#!/usr/bin/python3
""" Contains derived class Rectangle. """
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines class Rectangle. """

    def __init__(self, width, height):
        """ initializes instance of class Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
