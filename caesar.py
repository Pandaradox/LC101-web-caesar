# ########################################Caesarian Encryption
"""This program takes a string and rotates it by a provided integer
to encrypt the string.  The file also takes a rotation argument in the
terminal as a second parameter for argv."""


from helpers import alphabet_position, rotate_character
import string
import sys



def encrypt(text, rot = 13):
    secret = ""
    for char in text:
        secret += rotate_character(char, rot)
    return(secret)


def main():
    secret = input("Type a message:\n")
    if len(sys.argv) == 1:
        sys.argv.append(input("Rotate by:\n"))
    for check in sys.argv[1]:
        if (check in string.punctuation
                or check in string.whitespace
                or check in string.ascii_letters):
            print("ERROR: Keymord must consist of numerical characters!")
            sys.exit()
    print(encrypt(secret, int(sys.argv[1])))


if __name__ == "__main__":
    main()
