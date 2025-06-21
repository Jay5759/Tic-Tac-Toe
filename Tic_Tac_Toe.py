# Tic-Tac-Toe game implementation

def display(board):
    """Display the current state of the board."""
    for i in range(0,3):
        print("| ",end = "")
        for j in range(0,3):
            print(board[i][j],"| ", end = "")
        print("\n|---|---|---|")

def check_win(board):
    # check rows 
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            print(f"Player {'1' if row[0] == 'X' else '2'} wins!")
            return True
    
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            print(f"Player {'1' if board[0][col] == 'X' else '2'} wins!")
            return True
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        print(f"Player {'1' if board[0][0] == 'X' else '2'} wins!")
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        print(f"Player {'1' if board[0][2] == 'X' else '2'} wins!")
        return True
    
    # Check for a draw
    flag = True
    for row in board:
        if '-' in row:
            flag = False
    if flag:
        print("It's a draw!")
        return True

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    print("This is a two-player game.")
    print("Player 1 is 'X' and Player 2 is 'O'.")
    
    # Initialize the game board
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # A list to represent the board
    current_player = 1  # Start with Player 1

    # Main game loop
    while True:
        # Display the board
        display(board)

        if current_player == 1:
            print("Player 1's turn")
            while True: 
                x = int(input("Please enter the value from 1 to 9: "))
                x -= 1
                row = x // 3
                col = x % 3
                if x < 0 or x > 8:
                    print("Invalid Input, Enter again.")
                    continue
                elif board[row][col] == '-':
                    board[row][col] = 'X'
                    break
                else:
                    print("Invalid Input, Enter again.")
            current_player = 2  # Switch to Player 2
        else:
            print("Player 2's turn")
            while True: 
                x = int(input("Please enter the value from 1 to 9: "))
                x -= 1
                row = x // 3
                col = x % 3
                if x < 0 or x > 8:
                    print("Invalid Input, Enter again.")
                    continue
                elif board[row][col] == '-':
                    board[row][col] = 'O'
                    break
                else:
                    print("Invalid Input, Enter again.")
            current_player = 1  # Switch to Player 1
    
        flag = check_win(board)
        if flag:
            display(board)
            break
