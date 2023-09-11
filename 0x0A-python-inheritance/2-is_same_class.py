#!/usr/bin/python3
""" Contains function def is_same_class. """


def is_same_class(obj, a_class):
    """ Checks if an obj is of specified class.

    Args:
        obj (any): object to be checked
        a_class (type): specified class

    Returns:
        True if obj is of same class else False
    """
    if type(obj) is a_class:
        return True
    return False
