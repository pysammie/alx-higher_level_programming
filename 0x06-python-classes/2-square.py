#!/usr/bin/python3
""" A module of class Square with a size attribute.
"""


class Square:
    """ A class square with a size attribute. """

    def __init__(self, size=0):
        """ Initialization of class with instance.

        Args:
            size (int): size of square
        """
        self.set_size(size)

    def get_size(self):
        """ A getter method.

        Returns:
            size (int): size of square
        """
        return self.__size

    def set_size(self, size):
        """ A setter method.

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
