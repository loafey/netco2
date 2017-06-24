try:
    import getpass
    import hashlib
    import io
    import os.path
    import secrets
    import string
    import sys
    import time
    from io import BufferedReader
    from random import choice
    from socket import *
    from threading import Thread

    import clipboard
    from Crypto.Cipher import AES, PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
    from pyfiglet import Figlet
except ModuleNotFoundError:
    print("Library missing! Please run pip install -r requirements.txt")
    exit()


def Config():
    if os.path.isdir("Config") == False:
        os.mkdir("Config")
    if os.path.isfile("Config/Title.cfg") == False:
        title_file = open("Config/Title.cfg","w")
        title_file.write("Netco")
        title_file.close()
    if os.path.isfile("Config/Version.cfg") == False:
        _version = "0.4"
        version_file = open("Config/Version.cfg","w")
        version_file.write(_version)



def md5hash(file):
    hasher = hashlib.md5()
    with open(file, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha1hash(file):
    hasher = hashlib.sha1()
    with open(file, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha256hash(file):
    hasher = hashlib.sha256()
    with open(file, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def sha512hash(file):
    hasher = hashlib.sha512()
    with open(file, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def message():
    if os.path.isfile("Encrypted/message.txt"):
        os.remove("Encrypted/message.txt")

    os.system("cls" if os.name == "nt" else "clear")
    print(title__.renderText(_name))
    print("Encrypt text")
    print("")
    print("""Type the message you want to encrypt. Type --Done-- to be finished. You can't reverse writen lines!""")
    encrypt_out = "message"#input("Enter name of the encrypted text file: ")
    encrypt_out_file = open("Encrypted/message.txt","a")
    while True:
        text = input("> ")
        encrypt_out_file.write(text+"\n")
        if text == "--Done--":
            encrypt_out_file.close()
            encrypt_text = open("Encrypted/message.txt","rb").read()
            encrypt_text_out = open("Encrypted/message.txt.bin","wb")
            print("Input name of the recipent. End the name with '.public'!")
            recipient_key_file = input("> ")

            recipient_key = RSA.import_key(open("Public Keys/"+recipient_key_file).read())
            session_key = get_random_bytes(16)

            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            encrypt_text_out.write(cipher_rsa.encrypt(session_key))

            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(encrypt_text)
            [encrypt_text_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext)]
            encrypt_text_out.close()
            os.remove("Encrypted/message.txt")
            break

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
    print("Please choose a password length.")
    plength = (input("> "))
    alphabet = string.ascii_letters+string.digits+string.punctuation
    if check_float(plength) == True:
        try:
            plength = int(plength)
            password = str("".join(choice(alphabet) for x in range(plength)))
            print("")
            print(password)
            print("")
            print("Do you want to copy the password to the clipboard(y)?: ")
            copy_quest = input("> ")
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
    print(" 2. New key")
    print("  3. What is this software?")
    print("   4. Generate a password")
    print("    5. Exit")
    option = input("Select item: ")
    if check_float(option) == True:
        if option == "1":
            print("-----------------------------------")
            login()
        if option == "2":
            newkey()
        if option == "3":
            about()
        if option == "4":
            generate_password()
        if option == "5":
            quit()
        else:
            start_menu()
    else:
        start_menu()


def newkey():
    if os.path.isdir("Keys") == False:
        os.mkdir("Keys")
    if os.path.isdir("Public Keys") == False:
        os.mkdir("Public Keys")
    print("")
    print("We will now generate a key!")
    print("It is very important that you don't share your passphrase! For extra security your private key should also never be shared! In doing so may result in loss of privacy and personal information!")
    time.sleep(1)
    global secret_code
    print("Enter a usernam")
    user_name = input("> ")
    print("Enter password")
    secret_code = getpass.getpass("> ")
    print("Generating a key")
    global key
    global my_private
    global pkey
    try:
        key = RSA.generate(4096)
        my_private = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        pkey = key.publickey().exportKey()
        file_out = open("Keys/"+user_name, "wb")
        file_out.write(my_private)
        open("Public Keys/"+user_name+".public","wb").write(key.publickey().exportKey())
        file_out.close()
        print("Key generated...")
        time.sleep(3)
        start_menu()
    except:
        print("Something went wrong!")
        getpass.getpass("Press enter to return to main menu...")
        start_menu()

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
    print("  3. Encrypt text")
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
            print("Public key:")
            print("")
            print(str(pkey,"latin-1"))
            print("")
            print("md5: "+md5hash("Public Keys/"+user_name+".public"))
            print("sha1: "+sha1hash("Public Keys/"+user_name+".public"))
            print("sha256: "+sha256hash("Public Keys/"+user_name+".public"))
            print("sha512: "+sha512hash("Public Keys/"+user_name+".public"))
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
                print(str(my_private,"latin-1"))
                print("")
                print("md5: "+md5hash("Keys/"+user_name))
                print("sha1: "+sha1hash("Keys/"+user_name))
                print("sha256: "+sha256hash("Keys/"+user_name))
                print("sha512: "+sha512hash("Keys/"+user_name))
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
                let = getpass.getpass("Enter password: ")
                if let == secret_code:
                    os.remove("Keys/"+user_name)
                    os.remove("Keys/"+user_name+".public")
                    os.system("cls" if os.name == "nt" else "clear")
                    exit()
                else:
                    print("Wrong password!")
                    time.sleep(5)
                    menu()
            else:
                menu()

        if option == "7":
            os.system("cls" if os.name == "nt" else "clear")
            exit()
        else:
            print("enter something valid dumbhead")
            menu()
    else:
        menu()

def login():
    global attempt
    if os.path.isdir("Keys") == False:
        os.mkdir("Keys")
    if os.path.isdir("Public Keys") == False:
        os.mkdir("Public Keys")
    
    if os.path.isdir("Keys") == True:
        for dir, sub_dirs, files in os.walk("Keys"):
            if not files:
                print("Seems you have no keys")
                newkey()
        else:
            global secret_code
            global pkey
            global user_name
            print("Enter username.")
            user_name = input("> ")
            print("Enter password.")
            secret_code = getpass.getpass("> ")
            #secret_code = input("Enter passphrase: ")
            try:
                encoded_key = open("Keys/"+user_name, "rb").read()
            except:
                attempt = attempt+1
                print("User doesn't exist probably!")
                print("Attempts: "+str(attempt))
                time.sleep(0.3)
                print("")
                login()

            try:
                global key
                global my_private
                global pkey
                key = RSA.import_key(encoded_key, passphrase=secret_code)
                my_private = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
                pkey = key.publickey().exportKey()
                #open("my_public.pem","wb").write(key.publickey().exportKey())
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
    print("Enter name of the file you want to encrypt: ")
    try:
        encrypt_file = input("> ")
        encrypt_file_2 = (open(encrypt_file,"rb").read())
        encrypt_name = encrypt_file+".bin"
        encrypt_out = open("Encrypted/"+encrypt_name, "wb")
        print("Input name of file containing encryption key: ")
        recipient_key_file = input("> ")

        recipient_key = (RSA.import_key(open("Public Keys/"+recipient_key_file).read()))
        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        encrypt_out.write(cipher_rsa.encrypt(session_key))

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(encrypt_file_2) 
        [ encrypt_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext) ]
        getpass.getpass("Press enter to continue...")
        encrypt_out.close
    except FileNotFoundError:
        print("Seems like you entered a nonexistant file.")
        getpass.getpass("Press enter to return to main menu...")
        menu()

def decrypt_file():
    os.system("cls" if os.name == "nt" else "clear")
    if os.path.isdir("Decrypted") == False:
        os.mkdir("Decrypted")
    print(title__.renderText(_name))
    print("Decrypt file")
    print("")
    print("Enter name of file you want to decrypt.")
    try:
        decrypt_name = input("> ")
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
    except PermissionError:
        print("It seems like you entered something invalid.")
        getpass.getpass("Press enter to return to main menu...")
        menu()
    except FileNotFoundError:
        print("It seems like you entered a file that doesn't exist.")
        getpass.getpass("Press enter to return to main menu...")
        menu()


os.system("cls" if os.name == "nt" else "clear")
title__ = Figlet(font="slant")

_version = "0.5"
_name = "NETCO"

attempt = 0
start_menu()