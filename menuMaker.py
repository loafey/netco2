from pyfiglet import Figlet
import os
import time

def draw_Title_and_Undertext(title,undertext,font):
    title__ = Figlet(font=font)
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(title))
    print(undertext)
    print("")

def draw_Title(title,font):
    title__ = Figlet(font=font)
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(title))
    print("")

def Make_Tilt_Right(*items):
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        print(" "*x+str(x+1)+". "+items[x])

def Make_Tilt_Left(*items):
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        print(str(" "*(length-x))+str(x+1)+". "+items[x])

def Make(*items):
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        print(str(x+1)+". "+items[x])

def Make_Wave(*items):
    print("Type the corresponding number to do the corresponding action.")
    for x in range(len(items)):
        if float.is_integer(x/2) == True:
            print(str(x+1)+". "+items[x])
        else:
            print(" "+str(x+1)+". "+items[x])

def mlPrint(*items):
    for x in range(len(items)):
        print(items[x])