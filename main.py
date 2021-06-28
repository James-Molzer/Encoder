# this is a easy a simple coder/it will change that letters you put in to a code
# it can be translated back using my translator program

def encode(words):
    translation = ""
    for letter in words:
        if letter.lower() in "a":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "2"
        elif letter.lower() in "b":
            if letter.isupper():
                translation = translation + "`"
            else:
                translation = translation + "~"
        elif letter.lower() in "c":
            if letter.isupper():
                translation = translation + "x"
            else:
                translation = translation + "@"
        elif letter.lower() in "d":
            if letter.isupper():
                translation = translation + "^"
            else:
                translation = translation + "="
        elif letter.lower() in "e":
            if letter.isupper():
                translation = translation + "'"
            else:
                translation = translation + "L"
        elif letter.lower() in "f":
            if letter.isupper():
                translation = translation + "#"
            else:
                translation = translation + "/"
        elif letter.lower() in "g":
            if letter.isupper():
                translation = translation + "3"
            else:
                translation = translation + "|"
        elif letter.lower() in "h":
            if letter.isupper():
                translation = translation + "d"
            else:
                translation = translation + "6"
        elif letter.lower() in "i":
            if letter.isupper():
                translation = translation + "+"
            else:
                translation = translation + ">"
        elif letter.lower() in "j":
            if letter.isupper():
                translation = translation + "w"
            else:
                translation = translation + "$"
        elif letter.lower() in "k":
            if letter.isupper():
                translation = translation + "?"
            else:
                translation = translation + "["
        elif letter.lower() in "l":
            if letter.isupper():
                translation = translation + "-"
            else:
                translation = translation + "c"
        elif letter.lower() in "m":
            if letter.isupper():
                translation = translation + "4"
            else:
                translation = translation + ":"
        elif letter.lower() in "n":
            if letter.isupper():
                translation = translation + "<"
            else:
                translation = translation + "]"
        elif letter.lower() in "o":
            if letter.isupper():
                translation = translation + "."
            else:
                translation = translation + "M"
        elif letter.lower() in "p":
            if letter.isupper():
                translation = translation + "b"
            else:
                translation = translation + "{"
        elif letter.lower() in "q":
            if letter.isupper():
                translation = translation + ","
            else:
                translation = translation + "_"
        elif letter.lower() in "r":
            if letter.isupper():
                translation = translation + "%"
            else:
                translation = translation + "!"
        elif letter.lower() in "s":
            if letter.isupper():
                translation = translation + "*"
            else:
                translation = translation + "("
        elif letter.lower() in "t":
            if letter.isupper():
                translation = translation + "&"
            else:
                translation = translation + "1"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "a"
            else:
                translation = translation + "5"
        elif letter.lower() in "v":
            if letter.isupper():
                translation = translation + "k"
            else:
                translation = translation + "F"
        elif letter.lower() in "w":
            if letter.isupper():
                translation = translation + "7"
            else:
                translation = translation + "I"
        elif letter.lower() in "x":
            if letter.isupper():
                translation = translation + "v"
            else:
                translation = translation + "8"
        elif letter.lower() in "y":
            if letter.isupper():
                translation = translation + "g"
            else:
                translation = translation + "s"
        elif letter.lower() in "z":
            if letter.isupper():
                translation = translation + "p"
            else:
                translation = translation + ";"
        elif letter == "1":
            translation = translation + "B"
        elif letter == "2":
            translation = translation + "r"
        elif letter == "3":
            translation = translation + "j"
        elif letter == "4":
            translation = translation + "Y"
        elif letter == "5":
            translation = translation + "N"
        elif letter == "6":
            translation = translation + "o"
        elif letter == "7":
            translation = translation + "e"
        elif letter == "8":
            translation = translation + "U"
        elif letter == "9":
            translation = translation + "Z"
        elif letter == "0":
            translation = translation + "J"
        else:
            translation = translation + letter
    return translation

print(encode(input("enter your secret message: ")))

















