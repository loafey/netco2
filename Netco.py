from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from io import BufferedReader
from socket import *
from threading import Thread
import os.path
import getpass
import time
import sys
import io
import secrets
import string
import clipboard
from random import choice
from pyfiglet import Figlet
_version = "0.2"
_name = "Netco"

def message():
    host = "localhost"
    port = 8080
    bufsize = 1024
    addr = (host, addr)


def about():
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(_name))
    print("About")
    print("")
    print("Name: "+ _name)
    time.sleep(2)
    print("Version: "+_version)
    time.sleep(2)
    print("Creator: Samhamnam")
    time.sleep(2)
    getpass.getpass("Press enter to continue...")
    start_menu()

def generate_password():
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(_name))
    print("Generate a password")
    print("")
    plength = (input("Please choose a password length: "))
    alphabet = string.ascii_letters+string.digits+string.punctuation
    if check_float(plength) == True:
        try:
            plength = int(plength)
            password = str("".join(choice(alphabet) for x in range(plength)))
            print("")
            print(password)
            print("")
            copy_quest = input("Do you want to copy the password to the clipboard(y)?: ")
            if copy_quest == "y":
                clipboard.copy(password)
            else:
                start_menu()
        except MemoryError:
            print("Whoops seems it ran out of memory. Please try a smaller size.")
            getpass.getpass("Press enter to continue...")
def start_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(_name))
    print("Welcome to "+_name+"(Version: "+_version+")")
    print("")
    print("Type the corresponding number to do the corresponding action.")
    print("1. Login")
    print(" 2. What is this software?")
    print("  3. Generate a password")
    print("   4. Exit")
    option = input("Select item: ")
    if check_float(option) == True:
        if option == "1":
            print("-----------------------------------")
            login()
        if option == "2":
            about()
        if option == "3":
            generate_password()
        if option == "4":
            quit()
        else:
            start_menu()


def newkey():
    print("We will now generate a key!")
    print("It is very important that you don't share your passphrase! For extra security your private key should also never be shared! In doing so may result in loss of privacy and personal information!")
    time.sleep(1)
    global secret_code
    secret_code = getpass.getpass("Enter a passphrase: ")
    print("Generating a key")
    global key
    global my_private
    global pkey
    key = RSA.generate(4096)
    my_private = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
    pkey = key.publickey().exportKey()
    print("Key generated")
    file_out = open("my_private.bin", "wb")
    file_out.write(my_private)
    open("my_public.pem","wb").write(key.publickey().exportKey())
    file_out.close()

def check_float(option):
    try:
        float(option)
        return True
    except ValueError:
        return(False)

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(_name))
    print("Main menu")
    print("")
    print("Type the corresponding number to do the corresponding action.")
    print("1. Encrypt file")
    print(" 2. Decrypt file")
    print("  3. Send message")
    print("   4. View publickey")
    print("    5. View privatekey")
    print("     6. Delete key and exit")
    print("      7. Exit")
    option = input("Select item: ")
    if check_float(option) == True:
        if option == "1":
            encrypt_file()

        if option == "2":
            decrypt_file()

        if option == "3":
            message()

        if option == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print(title__.renderText(_name))
            print("Public key")
            print("")
            print(str(pkey))
            print("")
            getpass.getpass("Press enter to continue...")
            menu()

        if option == "5":
            os.system("cls" if os.name == "nt" else "clear")
            print(title__.renderText(_name))
            print("Private key")
            secret_code2=getpass.getpass("Password: ")
            print("")
            if secret_code2 == secret_code:
                print((my_private))
                print("")
                getpass.getpass("Press enter to continue...")
                menu()
            else:
                print("Wrong Password!")
                getpass.getpass("Press enter to continue...")
                menu()

        if option == "6":
            os.system("cls" if os.name == "nt" else "clear")
            print(title__.renderText(_name))
            print("Delete private key and exit")
            print("")
            del_ = input("Are you sure?(y): ")
            if del_ == "y":
                os.remove("my_private.bin")
                os.remove("my_public.pem")
                os.system("cls" if os.name == "nt" else "clear")
                exit()
            else:
                menu()

        if option == "7":
            os.system("cls" if os.name == "nt" else "clear")
            exit()
        else:
            print("enter something valid dumbhead")
            menu()

def login():
    global attempt
    if os.path.isfile("my_private.bin") == False:
        newkey()
    else:
        global secret_code
        global pkey
        secret_code = getpass.getpass("Enter passphrase: ")
        #secret_code = input("Enter passphrase: ")
        encoded_key = open("my_private.bin", "rb").read()
        try:
            global key
            global my_private
            global pkey
            key = RSA.import_key(encoded_key, passphrase=secret_code)
            my_private = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
            pkey = key.publickey().exportKey()
            open("my_public.pem","wb").write(key.publickey().exportKey())
            time.sleep(3)
            menu()
        except ValueError:
            attempt = attempt+1
            print("Wrong password probably!")
            print("Attempts: "+str(attempt))
            time.sleep(0.3)
            print("")
            login()
            

def encrypt_file():
    os.system("cls" if os.name == "nt" else "clear")
    if os.path.isdir("Encrypted") == False:
        os.mkdir("Encrypted")
    print(title__.renderText(_name))
    print("Encrypt file")
    print("")
    encrypt_file = input("Enter name of the file you want to encrypt: ")
    encrypt_file_2 = (open(encrypt_file,"rb").read())
    encrypt_name = encrypt_file+".bin"
    encrypt_out = open("Encrypted/"+encrypt_name, "wb")
    recipient_key_file = input("Input name of file containing encryption key: ")

    recipient_key = (RSA.import_key(open(recipient_key_file).read()))
    #recipient_key = bytes(recipient_key, "latin-1")
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypt_out.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(encrypt_file_2) 
    [ encrypt_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext) ]
    print(encrypt_file_2)
    #encrypt_file2.close
    encrypt_out.close
    #recipient_key_file.close
    #menu()

def decrypt_file():
    os.system("cls" if os.name == "nt" else "clear")
    if os.path.isdir("Decrypted") == False:
        os.mkdir("Decrypted")
    print(title__.renderText(_name))
    print("Decrypt file")
    print("")
    decrypt_name = input("Enter name of file you want to decrypt: ")
    decrypt_in = open("Encrypted/"+decrypt_name,"rb")
    privatekey = RSA.import_key(my_private,passphrase=secret_code)
    decrypt_out_name = decrypt_name.replace(".bin","")
    print(decrypt_out_name)

    enc_session_key, nonce, tag, ciphertext = \
        [ decrypt_in.read(x) for x in (privatekey.size_in_bytes(), 16, 16, -1) ]

    cipher_rsa = PKCS1_OAEP.new(privatekey)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    decrypt_save = open("Decrypted/"+decrypt_out_name,"wb")
    decrypt_save.write(data)
    decrypt_save.close()
    time.sleep(10)
    #menu()

os.system("cls" if os.name == "nt" else "clear")
title__ = Figlet(font="slant")
attempt = 0
start_menu()
