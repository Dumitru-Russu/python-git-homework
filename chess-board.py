from os import system

#tuple
SIZE = (8,8)


WKING   = 1
WQUEEN  = 2
WBISHOP = 3
WKNIGHT = 4
WROOK   = 5
WPAWN   = 6

BKING   = 12
BQUEEN  = 11
BBISHOP = 10
BKNIGHT = 9
BROOK   = 8
BPAWN   = 7


board = [
    [ 5, 4, 3 , 2 , 1 , 3 , 4, 5 ],
    [ 6, 6, 6 , 6 , 6 , 6 , 6, 6 ],
    [ 0, 0, 0 , 0 , 0 , 0 , 0, 0 ],
    [ 0, 0, 0 , 0 , 0 , 0 , 0, 0 ],
    [ 0, 0, 0 , 0 , 0 , 0 , 0, 0 ],
    [ 0, 0, 0 , 0 , 0 , 0 , 0, 0 ],
    [ 7, 7, 7 , 7 , 7 , 7 , 7, 7 ],
    [ 8, 9, 10, 11, 12, 10, 9, 8 ],

]

alphabet= "abcdefgh"
system("cls")

for i in range(SIZE[1]):
    print("    "+alphabet[i], end="")
print()


for ri in range(SIZE[0]):
    rc = SIZE[1]- ri

    print(" "+"-----"*SIZE[1])
    print(rc, end="")
    for ci in range(SIZE[1]):
        piece = " "
        if board[ri][ci]== BKING:
            piece = "♚"
        elif board[ri][ci]== BQUEEN:
            piece = "♛"
        elif board[ri][ci]== BBISHOP:
            piece = "♝"
        elif board[ri][ci]== BKNIGHT:
            piece = "♞"
        elif board[ri][ci]== BROOK:
            piece = "♜"
        elif board[ri][ci]== BPAWN:
            piece = "♟"
        elif board[ri][ci]== WKING:
            piece = "♔"
        elif board[ri][ci]== WQUEEN:
            piece = "♕"
        elif board[ri][ci]== WBISHOP:
            piece = "♗"
        elif board[ri][ci]== WKNIGHT:
            piece = "♘"
        elif board[ri][ci]== WROOK:
            piece = "♖"
        elif board[ri][ci]== WPAWN:
            piece = "♙"
            

        print(f"| {piece}  ", end="")

    print("|")

print(" "+"-----"*SIZE[1])
