def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\n+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+\n")

def check_win(board, player):
    """Checks if the current player has won."""
    # All possible winning combinations
    win_conditions = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return ' ' not in board

def get_player_move(player, board):
    """Gets and validates the player's move."""
    while True:
        try:
            move = int(input(f"Player '{player}', enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[move - 1] != ' ':
                print("That spot is already taken! Try again.")
            else:
                return move - 1
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Main function to play a single game of Tic-Tac-Toe."""
    board = [' '] * 9
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        
        # Get the current player's move
        move = get_player_move(current_player, board)
        board[move] = current_player

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player '{current_player}' wins!")
            game_over = True
        # Check for a draw
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        # Switch to the other player
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def main():
    """Main entry point for the application."""
    while True:
        play_game()
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    main()