# ########################################Vigenere Encryption
"""This program takes a string and rotates it by a provided keyword
to encrypt the string.  The file also takes a keyword argument in the
terminal as a second parameter for argv."""

import sys
import string


def encrypt(text, keyword):
    from helpers import alphabet_position, rotate_character
    key = []
    for k in keyword:
        key += [alphabet_position(k)]

    secret = ""
    keypos = 0

    for char in text:
        if char.isalpha():
            secret += rotate_character(char, key[keypos % len(key)])
            keypos += 1
        else:
            secret += char

    return(secret)


def main():
    message = input("Type a message:\n")
    if len(sys.argv) == 1:
        sys.argv.append(input("Encryption key:\n"))
    for check in sys.argv[1]:
        if (check in string.punctuation
                or check in string.whitespace
                or str(check) in string.digits):
            print("ERROR: Keyword must consist of alphabetical characters!")
            sys.exit()
    print(encrypt(message, sys.argv[1]))


if __name__ == "__main__":
    main()
