from os import system

def clear():
    system("cls")


def controls():
    print("use a,d,s,w - for movement")
    key = input(">> ")
    return key

