#!/usr/bin/python3
""" A module of class Square with size attribute
and Method Area """


class Square:
    """ A class Square. """

    def __init__(self, size=0):
        """ Initialization of class Square.

        Args:
            size (int): size of a side of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ defines the area of Square.

        Returns:
            current square area
        """
        if self.__size:
            return self.__size * self.__size
