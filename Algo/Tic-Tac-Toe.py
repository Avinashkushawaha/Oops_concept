# Function to print the game board
def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (i.e., a draw)
def is_draw(board):
    return all(cell != ' ' for cell in board)

# Function to handle the player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("This spot is already taken, choose a different spot.")
        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 9.")

# Main game function
def play_game():
    board = [' '] * 9  # Create an empty board
    current_player = 'X'  # X always starts

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board, current_player)
        print_board(board)

        # Check if the current player has won
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
