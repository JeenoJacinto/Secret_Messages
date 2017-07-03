import string
import random
from ciphers import Cipher


class Caesar(Cipher):
    """The Caesar Cipher class takes one arguement, the encryption letter"""
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase
        + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1]
        + string.ascii_uppercase

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)


class Alberti(Cipher):
    """The Alberti Cipher class takes one arguement, the encryption letter"""
    def __init__(self, pointer_letter):
        self.stabilis = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            ] * 2
        self.mobilis = ["a", "c", "3", "6", "e", "g", "k", "8", "l", "n", "p",
                        "5", "r", "t", "u", "z", "x", "4", "y", "9", "s", "0",
                        "o", "m", "q", "i", "h", "f", "2", "d", "b", "1", "w",
                        "7", "v", "j"] * 2
        self.pointer_letter = pointer_letter.lower()

    def spin_cipher(self, reference_letter):
        """This function creates two virtual wheels, stabalis and mobilis.
        It simulates rotating by re-assigning all the indices in relation
        to the pointer letter(encryption letter) and the reference letter
        which are the capital letters in the encrypted message.
        """
        set_mobilis = []
        set_stabilis = []
        mobilis_starting_index = 0
        mobilis_ending_index = 36
        stabilis_starting_index = 0
        stabilis_ending_index = 36
        for idx, letter in enumerate(self.mobilis):
            if letter == self.pointer_letter:
                mobilis_starting_index += idx
                mobilis_ending_index += idx
                break
        for idx, letter in enumerate(self.stabilis):
            if letter == reference_letter:
                stabilis_starting_index += idx
                stabilis_ending_index += idx
                break
        for stuff in self.mobilis[mobilis_starting_index:mobilis_ending_index]:
            set_mobilis.append(stuff)
        for stuff in self.stabilis[stabilis_starting_index:
                                   stabilis_ending_index]:
            set_stabilis.append(str(stuff).lower())
        # Sets encrypted letter and reference letter to index 0
        return {plain_text: cipher_text for plain_text, cipher_text in
                zip(set_stabilis, set_mobilis)}

    def encrypt(self, text):
        """Encryption process which takes one arguement: The message to encrypt.
        """
        key_to_word = {}
        encrypted_word = []
        word = list(text.lower())
        encrypted_word_string = []
        amount_of_reference_letters = int(len(word) / 5)
        word_range = list(range(len(word)))
        list_of_reference_letters = random.sample(self.stabilis[:26],
                                                  amount_of_reference_letters)
        index_insert = random.sample(word_range, amount_of_reference_letters)
        reference_letter_with_index_insert = {
            idx: ref_letter for idx, ref_letter in zip(
                index_insert, list_of_reference_letters)}
        starting_reference_letter = self.stabilis[random.randint(0, 25)]
        word.insert(0, starting_reference_letter)
        for idx, value in reference_letter_with_index_insert.items():
            word.insert(idx, value)
            # To add random reference letters to random points in the string.
            # This further encrypts the data.
        for char in word:
            if char in self.stabilis:
                # If capital letter found, mobilis is spun
                # Uses a new dict of assigned mobilis and stabilis values
                key_to_word = self.spin_cipher(char)
                encrypted_word.append(str(char))
            else:
                # Coverts plain text into encrypted text
                if char in self.mobilis:
                    for key, value in key_to_word.items():
                        if char == key:
                            encrypted_word.append(value)
                else:
                    encrypted_word.append(char)
        for char in encrypted_word:
            encrypted_word_string.append(str(char))
        return "".join(encrypted_word_string)

    def decrypt(self, text):
        """Decryption process which takes one arguement: The message to decrypt.
        """
        word = list(text)
        key_to_word = {}
        encrypted_word = []
        for char in word:
            if char in self.stabilis:
                # Detects capital letters to spin wheele
                key_to_word = self.spin_cipher(char)
            else:
                # Converts encrypted text to plain text
                if char in self.mobilis:
                    for key, value in key_to_word.items():
                        if char == value:
                            encrypted_word.append(str(key))
                else:
                    encrypted_word.append(str(char))
        return "".join(encrypted_word).lower()


class KeyWord(Cipher):
    """The KeyWord Cipher class takes one arguement, the encryption letter"""
    def __init__(self):
        self.regular_alpha = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"
            ]
        self.encrypted_alpha = ["c", "e", "g", "k", "l", "n", "p", "r",
                                "t", "u", "z", "x", "y", "s", "m", "q",
                                "i", "h", "f", "d", "b", "w", "v", "j",
                                "o", "a"]

    def get_key_value(self):
        """Creates a dict of keys and values from regular and encrypted alphabet
        """
        return {key: value for key, value in zip(self.regular_alpha,
                self.encrypted_alpha)}

    def encrypt(self, text):
        """Encryption process which takes one arguement: The message to encrypt.
        """
        word = list(text.lower())
        encrypted_word = []
        for char in word:
            # Converts plain text into encrypted text
            if char in self.encrypted_alpha:
                for key, value in self.get_key_value().items():
                    if char.upper() == key:
                        encrypted_word.append(value)
            else:
                encrypted_word.append(str(char))
        new_string = "".join(encrypted_word)
        return new_string.upper()

    def decrypt(self, text):
        """Decryption process which takes one arguement: The message to decrypt.
        """
        word = list(text.lower())
        encrypted_word = []
        for char in word:
            # Converts encrypted text into plain text
            if char in self.encrypted_alpha:
                for key, value in self.get_key_value().items():
                    if char == value:
                        encrypted_word.append(key)
            else:
                encrypted_word.append(str(char))
        new_string = "".join(encrypted_word)
        return new_string.upper()


class PolybiusSquare(Cipher):
    """The KeyWord Cipher class takes one arguement, the encryption letter"""
    def __init__(self):
        self.encryption_grid = {"c": 11, "e": 12, "g": 13, "k": 14, "l": 15,
                                "n": 21, "p": 22, "r": 23, "t": 24, "u": 25,
                                "z": 31, "x": 32, "y": 33, "s": 34, "m": 35,
                                "q": 41, "i": 42, "h": 43, "f": 44, "d": 45,
                                "b": 51, "w": 52, "v": 53, "o": 54, "a": 55}

    def encrypt(self, text):
        """Encryption process which takes one arguement: The message to encrypt.
        """
        word = list(text.lower())
        encrypted_word = []
        encrypted_string = ""
        for char in word:
            if char == 'j':
                # Makes an exception for the letter 'j' and converts it to 'i'
                encrypted_word.append(str(42))
            elif char == ' ':
                # Makes an exception for spaces
                encrypted_word.append(str(char))
            else:
                # Converts plain text into encrypted text
                for key, value in self.encryption_grid.items():
                    if char == key:
                        encrypted_word.append(str(value))
        encrypted_string += "".join(encrypted_word)
        return encrypted_string

    def decrypt(self, text):
        """Decryption process which takes one arguement: The message to decrypt.
        """
        word = list(text.lower())
        index_count = len(word)
        current_index = 0
        formatted_list = []
        encrypted_word = []
        encrypted_string = ""
        while current_index < index_count:
            # seperates spaces from message and decrypts numbers into letters
            try:
                int(word[current_index])
                formatted_list.append(int(word[current_index]
                                          + word[current_index + 1]))
                current_index += 2
            except ValueError:
                formatted_list.append(word[current_index])
                current_index += 1
        for char in formatted_list:
            if char == ' ':
                encrypted_word.append(char)
            else:
                for key, value in self.encryption_grid.items():
                    if char == value:
                        encrypted_word.append(key)
        encrypted_string += "".join(encrypted_word)
        return encrypted_string
