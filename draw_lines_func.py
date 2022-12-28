

def drawLine( length, direction ):
    if direction=='h':
        print('-'*length)
    elif direction=='v':
        print('|\n'*length)



drawLine(3,'v')
drawLine(5,'h')


