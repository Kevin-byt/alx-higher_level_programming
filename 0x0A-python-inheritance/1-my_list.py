#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """Implements sorted printing for the built-in list class.
    Args:
        list (int): A list object
    """

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
