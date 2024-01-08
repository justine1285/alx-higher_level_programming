#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specific class

    Args:
        obj: object to be checked
        a_class: type of class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
