#Checkmate
#Written by Roman Serna
#Distribution of this program is not allowed without the written permission of Roman Serna the Owner.

def Orientation():
    #All movements are in (x and y) or (x or y)
    #Z orienation is the same for all. 
    #With the ocassional Rook orientation being upside-down.
    #   Rook upside-down never in the initial position only
    #   if pawn moves +7moves or +6moves if initial move was +2
    #       If 4 or more pieces are moved at the same time than the board is being reset
    #       This can be an outlier if playing with time. (Time can be an indicator of outlier also speed)
    
    print(f"This function is to determine board orienation")
    #Look for the Rooks on the board and there location on the board will give orientation. 
    #There movemengt indicates parameter. 

def King():
    print(f"This is the White KING")
    #starts at E1
    #If moved it can only move to 
    #D1(-y), D2(x,-y), E2(x), F2(x,y), F1(y), 
    #Castling: G1(2y) or C1(-2y)
    

def Queen():
    print(f"This is the White Queen")

def KingB():
    print(f"This is the Black King")
    #starts at E8
    #If moved it can only move to 
    #D8(-y), D7(-x,-y), E(-x), F7(-x,y), F8(y)
    #Castling: G8(2y), C8(-2y)

def QueenB():
    print(f"This is the Black Queen")

def knightww():
    print(f"This is the knightww")
    #starts in g1
    #If moved it can only move to 
    #E2(x,-2y), F3(2X,-y), H3(2x, y)

def knightw():
    print(f"This is the knightw")
     #Starts in b1
    #If moved it can only move to
    #b3(2X,-y), c3(2x,y), d2(x,2y)

def knightb():
    print(f"This is the knighb")
    #Starts at b8
    #If moved it can only move to 
    #A6(-2x,-y), C6(-2x, y), D7(-x, 2y)

def knightbb():
    print(f"This is the knightbb")
    #Starts at g8
    #If moved it can only move to 
    #E7(-x,-2y), f6(-2x, -y), h6(-2x,y)

def rookw():
    print(f"This is the rookw")
    #if the rook moves it only moves in x or y
    
def rookww():
    print(f"This is the rookww")
    #if the rook moves it only moves in x or y

def rookb():
    print(f"This is the rookb")

def rookbb():
    print(f"This is the rookbb")

def bishopw():
    print(f"This is the bishopw")

def bishopww():
    print(f"This is the bishopsw")

def bishopb():
    print(f"This is the bishopb")

def bishopbb():
    print(f"This is the bishopbb")

def pawnsw():
     #Should each pawn have its own function or should each pawn be treated as an individual function
    print(f"These are the white pawns")
#if moved assume one space unless a secondary pawn moves twice as far.
#The rooks have created an outer parameter divide by 8 and that is the size of space. 
#compare the two distances to determine if one or two spaces were moved. 
#pawns are the first move to unlock further moves unless its a knight move
#   If pawn moves +7 it is promoted This pawn now acts as as a different piece. C
#   Check next movement to identify next move. 
# IF en-passant: then diagnal is allowed.
# IF diagnal then capturing pawn. 


def pawnsb():
    #Should each pawn have its own function or should each pawn be treated as an individual function
    print(f"These are the black pawns")
#if moved assume one space unless a secondary pawn moves twice as far.
#The rooks have created an outer parameter divide by 8 and that is the size of space. 
#compare the two distances to determine if one or two spaces were moved. 
#pawns are the first move to unlock further moves unless its a knight move

def check():
    print(f"The king is in check")

def mate():
    print(f"The game is over you have been checkmated")
#The game has to be restarted after this. 
#...?
