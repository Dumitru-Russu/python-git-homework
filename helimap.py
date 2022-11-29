SCALE  = 10

hX = 5
hY = 4

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY:
            map += "H "
        
        ## ZONA PERICOL   
        
        # elif y==hY and (x==hX-2 or x==hX-1 or x==hX+1 or x==hX+2):
        #     map += "x "
        # elif y==hY-1 and (x==hX-1 or x==hX or x==hX+1):
        #     map += "x "
        # elif y==hY+1 and (x==hX-1 or x==hX or x==hX+1):
        #     map += "x "
        
        ## ZONA PERICOL
            
        ## ZGOMOT SPORIT
        elif y==hY and (x==hX-2 or x==hX-1 or x==hX+1 or x==hX+2):
            map += "~ "
        elif y==hY-1 and (x==hX-2 or x==hX-1 or x==hX or x==hX+1 or x==hX+2):
            map += "~ "
        elif y==hY+1 and (x==hX-2 or x==hX-1 or x==hX or x==hX+1 or x==hX+2):
            map += "~ "
        elif y==hY-2 and (x==hX-1 or x==hX or x==hX+1):
            map += "~ "
        elif y==hY+2 and (x==hX-1 or x==hX or x==hX+1):
            map += "~ "
        ## ZGOMOT SPORIT
            
        
            
        else:
            map += "  "

    map += "\n"                

print(map)