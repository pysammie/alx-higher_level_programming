#!/usr/bin/python3
""" A module to demonstrate how to create a class
Square with a size attribute
"""


class Square:
    """ A class square with size attribute. """

    def __init__(self, size=None):
        """ Initialization of class square

        Args:
            size: size of square
        """
        self.__size = size
