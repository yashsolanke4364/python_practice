import random

board = [" "] * 9


def print_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}\n")


def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[i] == board[j] == board[k] == player for i, j, k in winning_combinations)


def check_draw():
    return " " not in board


def play():
    current_player = "X"
    while True:
        print_board()
        move = input(f"Player {current_player}, choose a position (1-9): ")
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid move")
            continue
        index = int(move) - 1
        if board[index] != " ":
            print("That spot is already taken")
            continue
        board[index] = current_player
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"


play()
