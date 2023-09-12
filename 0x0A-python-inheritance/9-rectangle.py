#!/usr/bin/python3
""" Contains derived class Rectangle. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines class Rectangle. """

    def __init__(self, width, height):
        """ Initializes instance of rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        """ String representation """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ computes area of rectangle. """
        return (self.__width * self.__height)
