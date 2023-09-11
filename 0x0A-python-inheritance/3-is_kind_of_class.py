#!/usr/bin/python3
""" Contains function def is_kind_of_class. """


def is_kind_of_class(obj, a_class):
    """ Checks if obj is instance of specified class/
    class inherited from specified class.

    Args:
        obj (any): object to be checked
        a_class (type): class to match

    Returns:
        True if obj is instance of class else False
    """

    if isinstance(obj, a_class):
        return True
    return False
