def alphabet_position(char):
    import string
    if char in string.ascii_uppercase:
        return((string.ascii_uppercase).find(char))
    elif char in string.ascii_lowercase:
        return((string.ascii_lowercase).find(char))


def rotate_character(char, rot):
    import string
    if char in string.ascii_uppercase:
        return((string.ascii_uppercase)[(alphabet_position(char)+rot) % 26])
    elif char in string.ascii_lowercase:
        return((string.ascii_lowercase)[(alphabet_position(char)+rot) % 26])
    else:
        return(char)

def main():
    import string
    import sys
    print(string.ascii_letters)
    final = ""
    print(sys.argv)
    if len(sys.argv) == 1:
        sys.argv.append(13)
    for char in string.ascii_letters:
        final += rotate_character(char, int(sys.argv[1]))
    print(final)


if __name__ == "__main__":
    main()
