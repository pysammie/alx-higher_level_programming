#!/usr/bin/python3
""" A module of class Square """


class Square:
    """ A class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a square

        Args:
            size (int): size of square
            position (int, int): coordinates of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: returns the size of square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: coordinates of square """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ defines area of square

        Returns:
            current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints square with # """
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(self.__position[1])]

            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for k in range(self.__size)]
                print("")
