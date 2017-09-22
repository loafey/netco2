# pylint: disable= W0612, C0103
"""
Randomly generates a password
"""
import getpass
import string
from random import choice
import clipboard


def createPassword(plength):
    """
    Randomly generates a password.
    Gives the option to copy it to the clipboard.
    """
    try:
        alphabet = string.ascii_letters+string.digits+string.punctuation
        plength = int(plength)
        password = str("".join(choice(alphabet) for x in range(plength)))
        print("")
        print(password)
        print("")
        print("Do you want to copy the password to the clipboard(y)?: ")
        copy_quest = input("> ")
        if copy_quest == "y":
            clipboard.copy(password)
    except MemoryError:
        print("Whoops seems it ran out of memory. Please try a smaller size.")
        getpass.getpass("Press enter to continue...")
