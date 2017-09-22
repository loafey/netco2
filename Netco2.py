"""
Pylint stuff
"""
# pylint: disable=I0011
# pylint: disable=W0106
# pylint: disable=W0601
# pylint: disable=W0621
# pylint: disable=W0702
# pylint: disable=C0103
# pylint: disable=R0912
# pylint: disable=R0915

try:
    import getpass
    import os.path
    import time

    import hashsums
    import menuMaker as mM
    import checker
    import createPassword

    from Crypto.Cipher import AES, PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes

except ModuleNotFoundError:
    print("Library missing! Please run pip install -r requirements.txt")
    exit()


def message():
    """
    Allows the user to encrypt some text
    """
    if os.path.isfile("Encrypted/message.txt"):
        os.remove("Encrypted/message.txt")

    mM.draw_Title_and_Undertext(_name, "Encrypt Text", _title_font)
    print("""Type the message you want to encrypt.""")
    print("Type --Done-- to be finished.")
    print("You can't reverse writen lines!")
    encrypt_out_file = open("Encrypted/message.txt", "a")
    while True:
        text = input("> ")
        encrypt_out_file.write(text+"\n")
        if text == "--Done--":
            encrypt_out_file.close()
            encrypt_text = open("Encrypted/message.txt", "rb").read()
            encrypt_text_out = open("Encrypted/message.txt.bin", "wb")
            print("Input name of the recipent. End the name with '.public'!")
            recipient_key_file = input("> ")

            recipient_key = RSA.import_key(open(
                "Public Keys/" + recipient_key_file).read())
            session_key = get_random_bytes(16)

            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            encrypt_text_out.write(cipher_rsa.encrypt(session_key))

            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(encrypt_text)
            [encrypt_text_out.write(x) for x in (
                cipher_aes.nonce, tag, ciphertext)]
            encrypt_text_out.close()
            os.remove("Encrypted/message.txt")
            break


def start_menu():
    """
    Displays the start menu
    """
    mM.draw_Title_and_Undertext(
        _name, "Welcome to " + _name + "Version: " + _version, _title_font)
    mM.Make_Tilt_Right(
        "Login", "New key", "About", "Generate a password", "Exit")
    option = input("Select item: ")
    if checker.Float_(option) is True:
        if option == "1":
            print("-----------------------------------")
            login()
        if option == "2":
            newkey()
        if option == "3":
            mM.draw_Title_and_Undertext(_name, "About", _title_font)
            mM.mlPrint(
                "Name: " + _name, "Version: " + _version, "Creator: Samhamnam")
            time.sleep(1)
            getpass.getpass("Press enter to continue...")
            start_menu()
        if option == "4":
            mM.draw_Title_and_Undertext(
                _name, "Generate a password", _title_font)
            print("Please choose a password length.")
            plength = (input("> "))
            if checker.Float_(plength) is True:
                createPassword.createPassword(plength)
                start_menu()
        if option == "5":
            quit()
        else:
            start_menu()
    else:
        start_menu()


def newkey():
    """
    Generates a new key for the user
    """
    if os.path.isdir("Keys") is False:
        os.mkdir("Keys")
    if os.path.isdir("Public Keys") is False:
        os.mkdir("Public Keys")
    print("")
    print("We will now generate a key!")
    print("It is very important that you don't share your Password!")
    print("For extra security your private key should also never be shared!")
    print("Doing so may result in loss of privacy and personal information!")
    time.sleep(1)
    global secret_code
    print("Enter a username")
    user_name = input("> ")
    print("Enter password")
    secret_code = getpass.getpass("> ")
    print("Generating a key")
    global key
    global my_private
    global pkey
    try:
        key = RSA.generate(4096)
        my_private = key.exportKey(
            passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
        pkey = key.publickey().exportKey()
        file_out = open("Keys/"+user_name, "wb")
        file_out.write(my_private)
        open("Public Keys/" + user_name + ".public", "wb").write(
            key.publickey().exportKey())
        file_out.close()
        print("Key generated...")
        time.sleep(3)
        start_menu()
    except:
        print("Something went wrong!")
        getpass.getpass("Press enter to return to main menu...")
        start_menu()


def menu():
    """
    Displays the main menu
    """
    mM.draw_Title_and_Undertext(_name, "Main Menu", _title_font)
    mM.Make_Tilt_Right(
        "Encrypt file",
        "Decrypt file",
        "Encrypt text",
        "View publickey",
        "View privatekey",
        "Delete key and exit",
        "Exit")
    option = input("Select item: ")
    if checker.Float_(option) is True:
        if option == "1":
            encrypt_file()

        if option == "2":
            decrypt_file()

        if option == "3":
            message()

        if option == "4":
            mM.draw_Title_and_Undertext(_name, "Public key:", _title_font)
            print(str(pkey, "latin-1"))
            print("")
            print("md5: "+hashsums.md5(
                "Public Keys/"+user_name+".public"))
            print("sha1: "+hashsums.sha1(
                "Public Keys/"+user_name+".public"))
            print("sha224: "+hashsums.sha224(
                "Public Keys/"+user_name+".public"))
            print("sha256: "+hashsums.sha256(
                "Public Keys/"+user_name+".public"))
            print("sha384: "+hashsums.sha384(
                "Public Keys/"+user_name+".public"))
            print("sha512: "+hashsums.sha512(
                "Public Keys/"+user_name+".public"))
            print("")
            getpass.getpass("Press enter to continue...")
            menu()

        if option == "5":
            mM.draw_Title_and_Undertext(_name, "Private Key:", _title_font)
            secret_code2 = getpass.getpass("Password: ")
            print("")
            if secret_code2 == secret_code:
                print(str(my_private, "latin-1"))
                print("")
                print("md5: " + hashsums.md5("Keys/"+user_name))
                print("sha1: " + hashsums.sha1("Keys/"+user_name))
                print("sha224: " + hashsums.sha224("Keys/"+user_name))
                print("sha256: " + hashsums.sha256("Keys/"+user_name))
                print("sha384: " + hashsums.sha384("Keys/"+user_name))
                print("sha512: " + hashsums.sha512("Keys/"+user_name))
                print("")
                getpass.getpass("Press enter to continue...")
                menu()
            else:
                print("Wrong Password!")
                getpass.getpass("Press enter to continue...")
                menu()

        if option == "6":
            mM.draw_Title_and_Undertext(
                _name, "Delete private key and exit.", _title_font)
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
    """
    Logins the user
    """
    if os.path.isdir("Keys") is False:
        os.mkdir("Keys")
    if os.path.isdir("Public Keys") is False:
        os.mkdir("Public Keys")

    if os.path.isdir("Keys") is True:
        for files in os.walk("Keys"):
            if not files:
                print("Seems you have no keys")
                newkey()
                break
        else:
            global secret_code
            global pkey
            global user_name
            print("Enter username.")
            user_name = input("> ")
            print("Enter password.")
            secret_code = getpass.getpass("> ")
            # secret_code = input("Enter Password: ")
            try:
                encoded_key = open("Keys/"+user_name, "rb").read()
            except:
                print("User doesn't exist probably!")
                time.sleep(0.3)
                print("")
                login()

            try:
                global key
                global my_private
                global pkey
                key = RSA.import_key(encoded_key, passphrase=secret_code)
                my_private = key.exportKey(
                    passphrase=secret_code,
                    pkcs=8, protection="scryptAndAES128-CBC")
                pkey = key.publickey().exportKey()
                # open("my_public.pem","wb").write(key.publickey().exportKey())
                time.sleep(3)
                menu()
            except ValueError:
                print("Wrong password probably!")
                time.sleep(0.3)
                print("")
                login()


def encrypt_file():
    """
    Enters the encryption function
    """
    if os.path.isdir("Encrypted") is False:
        os.mkdir("Encrypted")
    mM.draw_Title_and_Undertext(_name, "Encrypt File", _title_font)
    print("Enter name of the file you want to encrypt: ")
    try:
        encrypt_file = input("> ")
        encrypt_file_2 = (open(encrypt_file, "rb").read())
        encrypt_name = encrypt_file+".bin"
        encrypt_out = open("Encrypted/"+encrypt_name, "wb")
        print("Input name of file containing encryption key: ")
        recipient_key_file = input("> ")

        recipient_key = (RSA.import_key(open(
            "Public Keys/"+recipient_key_file).read()))
        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        encrypt_out.write(cipher_rsa.encrypt(session_key))

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(encrypt_file_2)
        [encrypt_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext)]
        getpass.getpass("Press enter to continue...")
        encrypt_out.close()
    except FileNotFoundError:
        print("Seems like you entered a nonexistant file.")
        getpass.getpass("Press enter to return to main menu...")
        menu()


def decrypt_file():
    """
    Allows the user to decrypt a file
    """
    if os.path.isdir("Decrypted") is False:
        os.mkdir("Decrypted")
    mM.draw_Title_and_Undertext(_name, "Decrypt File", _title_font)
    print("Enter name of file you want to decrypt.")
    try:
        decrypt_name = input("> ")
        decrypt_in = open("Encrypted/" + decrypt_name, "rb")
        privatekey = RSA.import_key(my_private, passphrase=secret_code)
        decrypt_out_name = decrypt_name.replace(".bin", "")
        print(decrypt_out_name)

        enc_session_key, nonce, tag, ciphertext = \
            [decrypt_in.read(x) for x in (
                privatekey.size_in_bytes(), 16, 16, -1)]

        cipher_rsa = PKCS1_OAEP.new(privatekey)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        decrypt_save = open("Decrypted/" + decrypt_out_name, "wb")
        decrypt_save.write(data)
        decrypt_save.close()
        time.sleep(10)
        # menu()
    except PermissionError:
        print("It seems like you entered something invalid.")
        getpass.getpass("Press enter to return to main menu...")
        menu()
    except FileNotFoundError:
        print("It seems like you entered a file that doesn't exist.")
        getpass.getpass("Press enter to return to main menu...")
        menu()


_version = "0.6"
_name = "Netco"
_title_font = "slant"
start_menu()
