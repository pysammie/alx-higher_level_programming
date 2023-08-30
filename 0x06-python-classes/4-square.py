#!/usr/bin/python3
""" A module of class Square. """


class Square:
    """ A class Square. """

    def __init__(self, size=0):
        """ Initialize square.

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """ int: size of square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Area of square

        Returns:
            Area of square
        """
        if self.__size:
            return self.__size * self.__size
