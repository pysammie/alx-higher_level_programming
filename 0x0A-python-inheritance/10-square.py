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
        super().__init__(size, size)
        self.__size = size
