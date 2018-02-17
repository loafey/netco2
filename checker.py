"""
A module used to check variables
"""


def Float_(option):
    """
    Checks if the variable works as a float
    """
    try:
        float(option)
        return True
    except ValueError:
        return False


def Int_(option):
    """
    Checks if the variable works as a interger
    """
    try:
        int(option)
        return True
    except ValueError:
        return False


def String_(option):
    """
    Checks if the variable works as a string
    """
    try:
        str(option)
        return True
    except ValueError:
        return False


def Bytes_(option):
    """
    Checks if the variable works as a byte object
    """
    try:
        bytes(option)
        return True
    except ValueError:
        return False


def List_(option):
    """
    Checks if the variable works as a list
    """
    try:
        list(option)
        return True
    except ValueError:
        return False


def Dict_(option):
    """
    Checks if the variable works as a dict
    """
    try:
        dict(option)
        return True
    except ValueError:
        return False
