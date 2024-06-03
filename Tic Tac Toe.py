def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 9.")

def update_board(board, move, player):
    row, col = (move - 1) // 3, (move - 1) % 3
    if board[row][col] in ['X', 'O']:
        print("This cell is already taken. Try again.")
        return False
    board[row][col] = player
    return True

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'")
    print("Take turns to place your mark on the board.")
    print("The first player to get 3 marks in a row, column, or diagonal wins!")
    print("Enter the number corresponding to the cell you want to mark (1-9).")
    
    while True:
        board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        current_player = 'X'
        game_ongoing = True
        
        while game_ongoing:
            print_board(board)
            move = get_move(current_player)
            
            if not update_board(board, move, current_player):
                continue
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                game_ongoing = False
                continue
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                game_ongoing = False
                continue
            
            current_player = 'O' if current_player == 'X' else 'X'

        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()