"""
A module useful for creating terminal a menu
"""
import os
from pyfiglet import Figlet


def draw_Title_and_Undertext(title, undertext, font):
    """
    Draws a title using pyfiglet and a text under
    """
    title__ = Figlet(font=font)
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(title))
    print(undertext)
    print("")


def draw_Title(title, font):
    """
    Just draws a title using pyfiglet
    """
    title__ = Figlet(font=font)
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(title))
    print("")


def Make_Tilt_Right(*items):
    """
    Draws a menu tilting to the right
    """
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        print(" "*x+str(x+1)+". "+items[x])


# def Make_Tilt_Left(*items):
#     print("Type the corresponding number to do the corresponding action.")
#     for x in range(len(items)):
#         print(str(" "*(length-x))+str(x+1)+". "+items[x])


def Make(*items):
    """
    Makes a normal menu
    """
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        print(str(x+1)+". "+items[x])


def Make_Wave(*items):
    """
    Makes a menu that waves
    """
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        if float.is_integer(x/2) is True:
            print(str(x+1)+". "+items[x])
        else:
            print(" "+str(x+1)+". "+items[x])


def mlPrint(*items):
    """
    Prints multiple lines on multiple lines
    """
    for x in range(len(items)):
        print(items[x])
