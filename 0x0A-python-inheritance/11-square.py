#!/usr/bin/python3
""" Contains derived class Square. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a class Square. """

    def __init__(self, size):
        """ Initializes a square

        Args:
            size (int): size of square
        """
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """ String representation """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """ Computes area of square """
        return self.__size * self.__size
