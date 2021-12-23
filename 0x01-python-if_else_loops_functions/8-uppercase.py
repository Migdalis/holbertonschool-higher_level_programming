#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def uppercase(str):
    for i in range(len(str)):
        print("{}".format(chr(ord(str[i]) - 32) if islower(str[i])
              else str[i]), end="")
    print("")
