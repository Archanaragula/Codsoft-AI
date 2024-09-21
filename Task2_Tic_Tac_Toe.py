import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()

# Check if the board has any available moves
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Evaluate the board to check if there is a winner
def evaluate(board):
    # Check rows for victory
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10

    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # No winner yet
    return 0

# Minimax algorithm to find the optimal move for the AI
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If the game has a winner, return the evaluated score
    if score == 10:
        return score
    if score == -10:
        return score

    # If there are no moves left and no winner, it's a tie
    if not is_moves_left(board):
        return 0

    # If this is the maximizer's (AI's) move (X)
    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                # Check if the spot is empty
                if board[i][j] == " ":
                    # Make the move
                    board[i][j] = 'X'

                    # Call minimax recursively to get the best value for this move
                    best = max(best, minimax(board, depth + 1, False))

                    # Undo the move
                    board[i][j] = " "
        return best

    # If this is the minimizer's (player's) move (O)
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                # Check if the spot is empty
                if board[i][j] == " ":
                    # Make the move
                    board[i][j] = 'O'

                    # Call minimax recursively to get the best value for this move
                    best = min(best, minimax(board, depth + 1, True))

                    # Undo the move
                    board[i][j] = " "
        return best

# Find the best move for the AI (X)
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    # Traverse all cells, evaluate minimax function for each empty cell
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                # Make the move
                board[i][j] = 'X'

                # Compute evaluation function for this move
                move_val = minimax(board, 0, False)

                # Undo the move
                board[i][j] = " "

                # If the value of the current move is better than the best value, update best_move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Check if there is a winner
def check_winner(board):
    score = evaluate(board)
    if score == 10:
        return "AI wins!"
    elif score == -10:
        return "Player wins!"
    elif not is_moves_left(board):
        return "It's a tie!"
    return None

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        while True:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = 'O'
                break
            else:
                print("Invalid move, please try again.")

        print("Player's Move:")
        print_board(board)

        # Check if player won
        winner = check_winner(board)
        if winner:
            print(winner)
            break

        # AI's move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print("AI's Move:")
        print_board(board)

        # Check if AI won
        winner = check_winner(board)
        if winner:
            print(winner)
            break

if __name__ == "__main__":
    play_tic_tac_toe()
