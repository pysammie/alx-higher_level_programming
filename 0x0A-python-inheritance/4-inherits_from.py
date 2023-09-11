#!/usr/bin/python3
""" Contains function def inherits_from. """


def inherits_from(obj, a_class):
    """ Checks if obj is only subclass of specified class.

    Args:
        obj (any): object to be checked
        a_class (type): specified class

    Returns:
        True if subclass only else False
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
