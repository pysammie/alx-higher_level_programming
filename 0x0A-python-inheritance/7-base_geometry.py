#!/usr/bin/python3
""" Contains class BaseGeometry. """


class BaseGeometry():
    """ Defines class with methods. """

    def area(self):
        """ Method not implemented. """

        raise Exception('area() not yet implemented')

    def integer_validator(self, name, value):
        """ Validates value of parameter.

        Args:
            name (str): name of parameter
            value (int): value of parameter

        Raises:
            TypeError if name not an integer
            ValueError if int <= 0
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
