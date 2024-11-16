import random

# Define the board size
BOARD_SIZE = 5

# Initialize the player's board and computer's board
player_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
computer_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
computer_hidden_board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Function to print the board
def print_board(board):
    print("  " + " ".join([str(i) for i in range(BOARD_SIZE)]))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))

# Function to randomly place the computer's battleship
def place_computer_battleship():
    ship_row = random.randint(0, BOARD_SIZE - 1)
    ship_col = random.randint(0, BOARD_SIZE - 1)
    computer_hidden_board[ship_row][ship_col] = "B"

# Function to take player's guess and update the board
def player_guess():
    while True:
        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Column: "))
            if guess_row not in range(BOARD_SIZE) or guess_col not in range(BOARD_SIZE):
                print("Invalid input. Please enter a number between 0 and 4.")
                continue
            if player_board[guess_row][guess_col] != " ":
                print("You already guessed that!")
                continue
            return guess_row, guess_col
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to check the player's guess
def check_guess(row, col):
    if computer_hidden_board[row][col] == "B":
        print("Hit!")
        player_board[row][col] = "X"
        return True
    else:
        print("Miss!")
        player_board[row][col] = "O"
        return False

# Main game loop
def play_game():
    place_computer_battleship()
    turns = 5
    
    while turns > 0:
        print("\nPlayer's Board:")
        print_board(player_board)
        guess_row, guess_col = player_guess()
        if check_guess(guess_row, guess_col):
            print("\nCongratulations! You sank the battleship!")
            break
        else:
            turns -= 1
            print(f"Turns left: {turns}")
            if turns == 0:
                print("\nGame Over! You're out of turns.")
                print("Computer's Board:")
                print_board(computer_hidden_board)
                break

# Run the game
play_game()
