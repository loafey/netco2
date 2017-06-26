import secrets
import string
from random import choice
import clipboard

def createPassword(plength):
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
    