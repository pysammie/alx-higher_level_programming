#!/usr/bin/python3
""" Contains class MyList. """


class MyList(list):
    """ Defines class MyList from baseclass list. """

    def print_sorted(self):
        """ Prints a sorted list. """

        print(sorted(self))
