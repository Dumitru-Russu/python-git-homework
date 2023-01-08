from map import *
from ui import *



while True:
    clear()
    printMap(gameMap)

    if gameMap[rr][rc-1]==3 or gameMap[rr][rc-2]==3 or gameMap[rr][rc+1]==3 or gameMap[rr][rc+2]==3 or\
       gameMap[rr-1][rc-1]==3 or gameMap[rr-1][rc-2]==3 or gameMap[rr-1][rc+1]==3 or gameMap[rr-1][rc+2]==3 or gameMap[rr-1][rc]==3 or\
       gameMap[rr-2][rc-1]==3 or gameMap[rr-2][rc-2]==3 or gameMap[rr-2][rc+1]==3 or gameMap[rr-2][rc+2]==3 or gameMap[rr-2][rc]==3 or\
       gameMap[rr+1][rc-1]==3 or gameMap[rr+1][rc-2]==3 or gameMap[rr+1][rc+1]==3 or gameMap[rr+1][rc+2]==3 or gameMap[rr+1][rc]==3 or\
       gameMap[rr+2][rc-1]==3 or gameMap[rr+2][rc-2]==3 or gameMap[rr+2][rc+1]==3 or gameMap[rr+2][rc+2]==3 or gameMap[rr+2][rc]==3:
        print("Danger!!! Mine detected!!!")

    key = controls()

    if key =='x':
        break



    gameMap[rr][rc] = 0  

    if key =='d' and rc<=8 and gameMap[rr][rc+1] != 1:
        rc += 1

    if key =='a' and rc>=1 and gameMap[rr][rc-1] != 1:
        rc -= 1

    if key =='s' and rr<=8 and gameMap[rr+1][rc] != 1:
        rr += 1


    if key =='w' and rr>=1 and gameMap[rr-1][rc] != 1:
        rr -= 1


    gameMap[rr][rc] = 2



