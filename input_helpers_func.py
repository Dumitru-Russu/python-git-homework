


def inputInt( message):
    value= int(input(message ))
    return value

def inputFloat( message):
    value= float(input(message ))
    return value

def inputBoolean( message):
    if message=="yes":
        return True
    else:
        return False

#####  la boolean asta trebuia de facut sau tot de convertit cu functia bool?


n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")


print( n + m)  