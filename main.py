# this is a easy a simple coder/ it will change that letters you put in to a code
#it can be  transtaled back useing my translator program

def encode(words):
    translation = ""
    for letter in words:
        if letter.lower() in "a":
            if letter.isupper():
                translation = translation + "x10"
            else:
                translation = translation + "x1"
        elif letter.lower() in "b":
            if letter.isupper():
                translation = translation + "~`"
            else:
                translation = translation + "~"
        elif letter.lower() in "c":
            if letter.isupper():
                translation = translation + "++"
            else:
                translation = translation + "+/"
        elif letter.lower() in "d":
            if letter.isupper():
                translation = translation + "z05"
            else:
                translation = translation + "Z5"
        elif letter.lower() in "e":
            if letter.isupper():
                translation = translation + "x20"
            else:
                translation = translation + "x2"
        elif letter.lower() in "f":
            if letter.isupper():
                translation = translation + "#/"
            else:
                translation = translation + "#|"
        elif letter.lower() in "g":
            if letter.isupper():
                translation = translation + "#3"
            else:
                translation = translation + "#4"
        elif letter.lower() in "h":
            if letter.isupper():
                translation = translation + "D6"
            else:
                translation = translation + "D8"
        elif letter.lower() in "i":
            if letter.isupper():
                translation = translation + "x30"
            else:
                translation = translation + "x3"
        elif letter.lower() in "j":
            if letter.isupper():
                translation = translation + "T4"
            else:
                translation = translation + "T8"
        elif letter.lower() in "k":
            if letter.isupper():
                translation = translation + "-7"
            else:
                translation = translation + "-4"
        elif letter.lower() in "l":
            if letter.isupper():
                translation = translation + "(}"
            else:
                translation = translation + "(]"
        elif letter.lower() in "m":
            if letter.isupper():
                translation = translation + "cv"
            else:
                translation = translation + "cp"
        elif letter.lower() in "n":
            if letter.isupper():
                translation = translation + "<."
            else:
                translation = translation + "<,"
        elif letter.lower() in "o":
            if letter.isupper():
                translation = translation + "x40"
            else:
                translation = translation + "x4"
        elif letter.lower() in "p":
            if letter.isupper():
                translation = translation + ":k"
            else:
                translation = translation + ":L"
        elif letter.lower() in "q":
            if letter.isupper():
                translation = translation + "^R"
            else:
                translation = translation + "^!"
        elif letter.lower() in "r":
            if letter.isupper():
                translation = translation + "@!"
            else:
                translation = translation + "@#"
        elif letter.lower() in "s":
            if letter.isupper():
                translation = translation + "37"
            else:
                translation = translation + "74"
        elif letter.lower() in "t":
            if letter.isupper():
                translation = translation + "94"
            else:
                translation = translation + "47"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "x50"
            else:
                translation = translation + "x5"
        elif letter.lower() in "v":
            if letter.isupper():
                translation = translation + "*0"
            else:
                translation = translation + "*1"
        elif letter.lower() in "w":
            if letter.isupper():
                translation = translation + "%1"
            else:
                translation = translation + "%9"
        elif letter.lower() in "x":
            if letter.isupper():
                translation = translation + "51"
            else:
                translation = translation + "5!"
        elif letter.lower() in "y":
            if letter.isupper():
                translation = translation + "x0"
            else:
                translation = translation + "x9"
        elif letter.lower() in "z":
            if letter.isupper():
                translation = translation + "?9"
            else:
                translation = translation + "?1"
        else:
            translation = translation + letter
    return translation

print(encode(input("enter your secret message: ")))

















