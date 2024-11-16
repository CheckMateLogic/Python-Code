#This is my first Game Program
#Written/Developed Entirely by Roman Serna
#Date: 2024/10/19, 12:53PM
#The objective of this code is to make a Chess Game

board = ['X'] * 25
count = len(board)

#Initiating 5X5 Board
print(board)


board[20:25]=['P', 'P', 'P', 'P', 'P']

# Function to display the board
def display_board(board):
    for i in range(5):
        print(" ".join(board[i*5:(i+1)*5]))

display_board(board)  # Display initial board



class scene:


    def __init__(self):
        self.move_attempts= 0

    def display_info(self, movement):
        if movement == "1A2": 
            # instead of a single specific character have it search a matrix/list to make sure the move is inside the board/list.
            board[15]='P'
            board[20]='X'
            print("Updated Board:")
            display_board(board)
        else:
            print('Not an allowed move, Please use Chess Notation/Algebraic-Chess-Notation')
            self.move_attempts +=1
            if self.move_attempts < 5:
                movement = input("Please make a move:")
                self.display_info(movement)
            else:
                print("Too many invalid attempts. Exiting move sequence.")
            #I need to set a input counter to keep the user from going on an infinte loop, counter will break after 5.

scene = scene()
movement = input("Please make a move: ")
scene.display_info(movement)
# Mapping for columns and rows
columns = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
rows = {'1': 4, '2': 3, '3': 2, '4': 1, '5': 0}

def convert_move(move):
    if len(move) == 3 and move[1] in columns and move[2] in rows:
        start_col = columns[move[0]]
        start_row = rows[move[1]]
        end_row = rows[move[2]]
        return start_row * 5 + start_col, end_row * 5 + start_col
    return None, None

class scene:
    def __init__(self):
        self.move_attempts = 0

    def display_info(self, movement):
        start, end = convert_move(movement)
        if start is not None and end is not None and board[start] == 'P' and board[end] == 'X':
            board[end] = 'P'
            board[start] = 'X'
            print("Updated Board:")
            display_board(board)
        else:
            print('Not an allowed move, Please use Chess Notation/Algebraic-Chess-Notation')
            self.move_attempts += 1
            if self.move_attempts < 5:
                movement = input("Please make a move: ")
                self.display_info(movement)
            else:
                print("Too many invalid attempts. Exiting move sequence.")

scene = scene()
movement = input("Please make a move: ")
scene.display_info(movement)