# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |")

# Function to check if the game is over
def is_game_over():
    # Check for a win
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True

    # Check for a tie
    if " " not in board:
        return True

    return False

# Main game loop
def tic_tac_toe_game():
    current_player = "X"
    while True:
        display_board()
        print(f"Player {current_player}, enter your move (1-9): ")
        move = int(input()) - 1

        # Check if the move is valid
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = current_player

        # Check if the game is over
        if is_game_over():
            display_board()
            if " " not in board:
                print("It's a tie!")
            else:
                print(f"Player {current_player} wins!")
            break

        # Switch to the other player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Start the game
tic_tac_toe_game()
