#!/usr/bin/python3
""" A module of class Square """


class Square:
    """ A class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a square

        Args:
            size (int): size of square
            position (tuple): coordinates of square
        """
        self.__size = size
        self.__position = position

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
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, value) for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
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
            flag_i, flag_j = 1, 1
            for i in range(self.__size):
                if self.__position[1] > 0 and flag_i == 1:
                    print("" * self.__position[1])
                    flag_i = 0
                for j in range(self.__size):
                    if self.__position[0] > 0 and flag_j == 1:
                        print(" " * self.__position[0], end="")
                        flag_j = 0
                    print("#", end="")
                print("")
                flag_j = 1
