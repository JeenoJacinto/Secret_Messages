from cipher_type import Alberti
from cipher_type import KeyWord
from cipher_type import PolybiusSquare
import os
import string
import random


def clear():
    """Clears the screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def five_block(text):
    """Takes a string and turns words into 5 character blocks"""
    character_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                      "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                      "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3",
                      "4", "5", "6", "7", "8", "9"]
    secure_list = []
    number_of_blocks = len(text.split(" "))
    count = 0
    while count < number_of_blocks:
        # Creates a randomized 5 character block
        secure_list.append(character_list[random.randint(0, 35)])
        secure_list.append(character_list[random.randint(0, 35)])
        secure_list.append(character_list[random.randint(0, 35)])
        secure_list.append(character_list[random.randint(0, 35)])
        secure_list.append(character_list[random.randint(0, 35)])
        secure_list.append(" ")
        count += 1
    del secure_list[-1]
    return "".join(secure_list)


def use_alberti(encrypted_messages, message_type, loop):
    """Starts the Alberti Cipher Loop"""
    done = True
    while done:
        # Alberti Cipher Menu
        clear()
        print("-Alberti Cipher Selected-\n")
        print("1: Encrypt")
        print("2: Decrypt")
        print("3: Previous Menu\n")
        print("\nPlease enter the number of the option"
              + " you wish to choose.")
        user_input = input(">")
        if user_input.upper() == '3':
            # Return to Main Menu
            loop.append("done")
            done = False
            break
        elif user_input.upper() == '1':
            # Encryption Process
            correct_input = True
            selected_pointer_letter = ""
            while correct_input:
                # Loop for getting a valid encryption letter
                clear()
                print("To encrypt with an Alberti Cipher you must select an"
                      + " encription letter.")
                print("This letter must be disclosed to the"
                      + " recipient in order to decrypt the message.\n")
                print("Please enter a letter of your choice:")
                pointer_letter = input(">").lower()
                if len(pointer_letter) == 1:
                    if pointer_letter in string.ascii_lowercase:
                        selected_pointer_letter += pointer_letter
                        correct_input = False
                    else:
                        print("Invalid Encryption Letter")
                        input("Press Return")
                else:
                    print("Invalid Encryption Letter")
                    input("Press Return")
            else:
                clear()
                alberti = Alberti(selected_pointer_letter)
                print("This modified Alberti Cipher is able to encrypt every"
                      + " letter and number.")
                print("Only letters and numbers will be encrypted. \nOther"
                      + " characters will remain unencrypted.\n")
                print("Selected Encryption Letter: {}".format(
                      selected_pointer_letter))
                print("Please enter the message you wish to encrypt.")
                text = input(">")
                # User types in message to be decrypted
                encrypted_message = alberti.encrypt(text)
                while True:
                    message_type.append("Alberti Cipher")
                    encrypted_messages.append(encrypted_message)
                    while True:
                        # Prompts user to display message in 5 character blocks
                        clear()
                        print("Would you like to display message"
                              + " in 5 character blocks?\n")
                        print("1: Yes")
                        print("2: No")
                        print("\nPlease enter the number of the option"
                              + " you wish to choose.")
                        user_chosen_option = input(">")
                        if user_chosen_option == "1":
                            encrypted_message = five_block(text)
                            break
                        elif user_chosen_option == "2":
                            break
                        else:
                            print("Invalid Input")
                            input("Press Return")
                    clear()
                    print("Your encrypted message: {}".format(
                        encrypted_message))
                    print("Selected Encryption Letter: {}\n".format(
                        selected_pointer_letter))
                    print("Encrypted message has been added to your encrypted"
                          + " messages folder\n")
                    print("When decrypting this message, remember which"
                          + " encryption letter you used.")
                    print("You will be prompted for it during the decryption"
                          + " process.")
                    input("Press Return")
                    done = False
                    break
        elif user_input.upper() == "2":
            # Decryption Process
            selected_pointer_letter = ""
            correct_input = True
            while correct_input:
                # Loop to get a valid encryption letter
                clear()
                print("Please enter encription letter")
                pointer_letter = input(">").lower()
                if len(pointer_letter) == 1:
                    if pointer_letter in string.ascii_lowercase:
                        selected_pointer_letter += pointer_letter
                        correct_input = False
                    else:
                        print("Invalid Encryption Letter")
                        input("Press Return")
                else:
                    print("Invalid Encryption Letter")
                    input("Press Return")
            else:
                clear()
                alberti = Alberti(selected_pointer_letter)
                decryption = True
                while decryption:
                    print("Alberti Message Decryption\n")
                    print("1: Encrypted Messages Folder")
                    print("2: Manually type message to decrypt\n")
                    print("\nPlease enter the number of the option"
                          + " you wish to choose.")
                    choice = input(">")
                    if choice == "1":
                        # User chooses message from folder
                        clear()
                        alberti_encrypted_messages = []
                        for key, value in enumerate(encrypted_messages):
                            if message_type[key] == "Alberti Cipher":
                                alberti_encrypted_messages.append(value)
                                # Only Alberti encrypted messages are shown
                        if len(alberti_encrypted_messages) < 1:
                            print(
                                "No Alberti Cipher encrypted messages found.")
                            input("Press Return")
                            break
                        else:
                            while True:
                                clear()
                                options = []
                                for key, value in enumerate(
                                        alberti_encrypted_messages):
                                    print("{}: {}".format(key + 1, value))
                                    options.append(key + 1)
                                print("\nPlease enter the number of the"
                                      + " message you wish to decrypt.")
                                user_choice = input(">")
                                try:
                                    int(user_choice)
                                    if int(user_choice) in options:
                                        print("Message Decrypted:\n")
                                        print(alberti.decrypt(
                                            alberti_encrypted_messages
                                            [int(user_choice) - 1]))
                                        input("\nPress Return")
                                        decryption = False
                                        break
                                    else:
                                        print("Invalid Input")
                                        input("Press Return")
                                except ValueError:
                                    print("Invalid Input")
                                    input("Press Return")
                    elif choice == "2":
                        # User manually types in message to decrypt
                        clear()
                        print("Encryption Letter: {}\n".format(
                            selected_pointer_letter))
                        print("Please type the message you wish to decrypt.")
                        user_message = input(">")
                        print("\nMessage Decrypted:\n")
                        print(alberti.decrypt(user_message))
                        input("\nPress Return")
                        decryption = False
                        break


def use_polybius_square(encrypted_messages, message_type, loop):
    """Starts the Polybius Square Cipher Loop"""
    done = True
    while done:
        # Polybius Square Cipher Menu
        clear()
        print("-Polybius Square Cipher Selected-\n")
        print("1: Encrypt")
        print("2: Decrypt")
        print("3: Previous Menu\n")
        print("\nPlease enter the number of the option"
              + " you wish to choose.")
        user_input = input(">")
        if user_input.upper() == '3':
            # Option to get to main menu
            loop.append("done")
            done = False
            break
        elif user_input.upper() == '1':
            # Encryption Process
            while True:
                clear()
                polybius_square = PolybiusSquare()
                print("This is a traditional Polybius Square Cipher.\n")
                print("This cipher only takes in letters and spaces.")
                print("5x5 Polybius Square Ciphers only uses 25/26 letters")
                print("The letter J is replaced with I as a result\n")
                print("Please enter the message you wish to encrypt.")
                text = input(">")
                checker = True
                place_holder = 0
                for char in text:
                    # Loop to get a message with only letters and spaces
                    if char == ' ':
                        place_holder += 1
                    else:
                        if char.lower() in string.ascii_lowercase:
                            place_holder += 1
                        else:
                            checker = False
                if checker:
                    break
                else:
                    clear()
                    print("Message must only contain letters and spaces.")
                    input("Press Return")
            while True:
                clear()
                encrypted_message = polybius_square.encrypt(text)
                message_type.append("Polybius Square Cipher")
                encrypted_messages.append(encrypted_message)
                while True:
                    # Prompts user to display message using 5 character blocks
                    clear()
                    print("Would you like to display message"
                          + " in 5 character blocks?\n")
                    print("1: Yes")
                    print("2: No")
                    print("\nPlease enter the number of the option"
                          + " you wish to choose.")
                    user_chosen_option = input(">")
                    if user_chosen_option == "1":
                        encrypted_message = five_block(text)
                        break
                    elif user_chosen_option == "2":
                        break
                    else:
                        print("Invalid Input")
                        input("Press Return")
                clear()
                print("Your encrypted message: {}".format(encrypted_message))
                print("Encrypted message has been added to your encrypted"
                      + " messages folder\n")
                input("Press Return")
                done = False
                break
        elif user_input.upper() == "2":
            # Decryption Process
            clear()
            polybius_square = PolybiusSquare()
            decryption = True
            while decryption:
                print("Polybius Square Cipher Message Decryption\n")
                print("1: Encrypted Messages Folder")
                print("2: Manually type message to decrypt\n")
                print("\nPlease enter the number of the option"
                      + " you wish to choose.")
                choice = input(">")
                if choice == "1":
                    # Uses saved messages from folder
                    clear()
                    polybius_square_encrypted_messages = []
                    for key, value in enumerate(encrypted_messages):
                        if message_type[key] == "Polybius Square Cipher":
                            polybius_square_encrypted_messages.append(value)
                    if len(polybius_square_encrypted_messages) < 1:
                        print("No Polybius Square Cipher encrypted messages"
                              + "found.")
                        input("Press Return")
                        break
                    else:
                        while True:
                            # User chooses which message to decrypt
                            clear()
                            options = []
                            for key, value in enumerate(
                                    polybius_square_encrypted_messages):
                                print("{}: {}".format(key + 1, value))
                                options.append(key + 1)
                            print("\nPlease enter the number of the"
                                  + " message you wish to decrypt.")
                            user_choice = input(">")
                            try:
                                int(user_choice)
                                if int(user_choice) in options:
                                    print("Message Decrypted:\n")
                                    print(polybius_square.decrypt(
                                        polybius_square_encrypted_messages[int(
                                            user_choice) - 1]))
                                    input("\nPress Return")
                                    decryption = False
                                    break
                                else:
                                    print("Invalid Input")
                                    input("Press Return")
                            except ValueError:
                                print("Invalid Input")
                                input("Press Return")
                elif choice == "2":
                    # User manually types in a message to decrypt
                    message_check = True
                    while message_check:
                        clear()
                        polybius_square = PolybiusSquare()
                        print("Please type the message you wish to decrypt.")
                        text = input(">")
                        checker = 0
                        number_list = []
                        for char in text:
                            try:
                                int(char)
                                number_list.append(char)
                            except ValueError:
                                    if char != " ":
                                        checker += 1
                        if checker == 0:
                            if len(number_list) % 2 == 0:
                                break
                            else:
                                print("Invalid Message")
                                input("Press Return")
                        else:
                            clear()
                            print("Message must only contain numbers"
                                  + " and spaces.")
                            input("Press Return")

                    print("\nMessage Decrypted:\n")
                    print(polybius_square.decrypt(text))
                    input("\nPress Return")
                    decryption = False
                    break


def use_key_word(encrypted_messages, message_type, loop):
    """Starts the Key Word Cipher Loop"""
    done = True
    while done:
        # Key Word Cipher Menu
        clear()
        print("-Key Word Cipher Selected-\n")
        print("1: Encrypt")
        print("2: Decrypt")
        print("3: Previous Menu\n")
        print("\nPlease enter the number of the option"
              + " you wish to choose.")
        user_input = input(">")
        if user_input.upper() == '3':
            # User returns to previous menu
            loop.append("done")
            done = False
            break
        elif user_input.upper() == '1':
            # Encryption Process
            clear()
            key_word = KeyWord()
            print("This is a basic Key Word Cipher.")
            print("This cipher only encrypts letters.")
            print("Any other character will not be encrypted\n")
            print("Please enter the message you wish to encrypt.")
            text = input(">")
            # User types in message to encrypt
            while True:
                clear()
                encrypted_message = key_word.encrypt(text)
                message_type.append("Key Word Cipher")
                encrypted_messages.append(encrypted_message)
                while True:
                    # Prompts user to display message using 5 character blocks
                    clear()
                    print("Would you like to display message"
                          + " in 5 character blocks?\n")
                    print("1: Yes")
                    print("2: No")
                    print("\nPlease enter the number of the option"
                          + " you wish to choose.")
                    user_chosen_option = input(">")
                    if user_chosen_option == "1":
                        encrypted_message = five_block(text)
                        break
                    elif user_chosen_option == "2":
                        break
                    else:
                        print("Invalid Input")
                        input("Press Return")
                clear()
                print("Your encrypted message: {}".format(encrypted_message))
                print("Encrypted message has been added to your encrypted"
                      + " messages folder\n")
                input("Press Return")
                done = False
                break
        elif user_input.upper() == "2":
            # Decryption Process
            clear()
            key_word = KeyWord()
            decryption = True
            while decryption:
                print("Key Word Cipher Message Decryption\n")
                print("1: Encrypted Messages Folder")
                print("2: Manually type message to decrypt\n")
                print("\nPlease enter the number of the option"
                      + " you wish to choose.")
                choice = input(">")
                if choice == "1":
                    # User uses messages from encrypted messages folder
                    clear()
                    key_word_encrypted_messages = []
                    for key, value in enumerate(encrypted_messages):
                        if message_type[key] == "Key Word Cipher":
                            key_word_encrypted_messages.append(value)
                            # Filters out messages not encrypted with Key Word
                    if len(key_word_encrypted_messages) < 1:
                        print("No Key Word Cipher encrypted messages found.")
                        input("Press Return")
                        break
                    else:
                        while True:
                            clear()
                            options = []
                            for key, value in enumerate(
                                    key_word_encrypted_messages):
                                print("{}: {}".format(key + 1, value))
                                options.append(key + 1)
                            print("\nPlease enter the number of the"
                                  + " message you wish to decrypt.")
                            user_choice = input(">")
                            try:
                                int(user_choice)
                                if int(user_choice) in options:
                                    print("Message Decrypted:\n")
                                    print(key_word.decrypt(
                                        key_word_encrypted_messages
                                        [int(user_choice) - 1]))
                                    input("\nPress Return")
                                    decryption = False
                                    break
                                else:
                                    print("Invalid Input")
                                    input("Press Return")
                            except ValueError:
                                print("Invalid Input")
                                input("Press Return")
                elif choice == "2":
                    # User manually types in message to decrypt
                    clear()
                    key_word = KeyWord()
                    print("Please type the message you wish to decrypt.")
                    text = input(">")
                    print("\nMessage Decrypted:\n")
                    print(key_word.decrypt(text))
                    input("\nPress Return")
                    decryption = False
                    break


one_time_pad = False
encrypted_messages = []
message_type = []
while True:
    # Main Menu Loop
    encrypted_message_folder = {key: value for key, value in zip(
        message_type, encrypted_messages)}
    clear()
    print("Top Secret Message Encrypter/Decrypter\n \n \n")
    print("1: Alberti Cipher - Decryption Difficulty 10/10")
    print("2: Polybius Square Cipher - Decryption Difficulty 7/10")
    print("3: Key Word Cipher - Decryption Difficulty 2/10")
    print("4: View Encrypted Messages Folder")
    print("5: Quit/Done")
    print("\n \n \nPlease enter the number of the cipher/option"
          + " you wish to choose.")
    option_choice = input(">")
    if option_choice == "1":
        loop = []
        while len(loop) == 0:
            clear()
            if one_time_pad:
                encrypted_message_folder = {key: value for key, value in zip(
                    message_type, encrypted_messages)}
                use_alberti(encrypted_messages, message_type, loop)
            else:
                print("Please enter password for one time pad\n")
                password = input(">")
                if password == "1234":
                    one_time_pad = True
                else:
                    print("Access Denied")
                    press_return = input("Press Return")
                    break
    elif option_choice == "2":
        loop = []
        while len(loop) == 0:
            clear()
            if one_time_pad:
                encrypted_message_folder = {key: value for key, value in zip(
                    message_type, encrypted_messages)}
                use_polybius_square(encrypted_messages, message_type, loop)
            else:
                print("Please enter password for one time pad\n")
                password = input(">")
                if password == "1234":
                    one_time_pad = True
                else:
                    print("Access Denied")
                    press_return = input("Press Return")
                    break
    elif option_choice == "3":
        loop = []
        while len(loop) == 0:
            clear()
            if one_time_pad:
                encrypted_message_folder = {key: value for key, value in zip(
                    message_type, encrypted_messages)}
                use_key_word(encrypted_messages, message_type, loop)
            else:
                print("Please enter password for one time pad\n")
                password = input(">")
                if password == "1234":
                    one_time_pad = True
                else:
                    print("Access Denied")
                    press_return = input("Press Return")
                    break
    elif option_choice == "4":
        # Option to View Folder
        clear()
        if len(encrypted_messages) == 0:
            print("You have 0 messages!")
        else:
            print("Encrypted Messages:\n")
            for key, value in enumerate(encrypted_messages):
                print("Message Type: {}\n{}\n".format(
                    message_type[key], encrypted_messages[key]))
        press_return = input("Press Return")
    elif option_choice == "5":
        # Option to quit program
        clear()
        break
