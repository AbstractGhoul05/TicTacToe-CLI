from os import system, name
from time import sleep

def clear():
    # sleep(2)
    if name == "nt":
        system('cls')
    else:
        system('clear')

def print_board(board, avail):
    print("\n")
    print("   Available Moves        TIC-TAC-TOE   \n")
    print(f"    {avail[7]}  |  {avail[8]}  |  {avail[9]}        {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("  -----------------    -----------------")
    print(f"    {avail[4]}  |  {avail[5]}  |  {avail[6]}        {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("  -----------------    -----------------")
    print(f"    {avail[1]}  |  {avail[2]}  |  {avail[3]}        {board[1]}  |  {board[2]}  |  {board[3]}  ")

def place_marker(board, avail, marker, position):
    if board[position] == ' ':
        board[position] = marker
        avail[position] = ' '
    else:
        print("The position has already been taken")

def win_check(board, mark):
    return ((board[7] ==  board[8] ==  board[9] == mark) or
    (board[4] ==  board[5] ==  board[6] == mark) or
    (board[1] ==  board[2] ==  board[3] == mark) or
    (board[7] ==  board[4] ==  board[1] == mark) or
    (board[8] ==  board[5] ==  board[2] == mark) or
    (board[9] ==  board[6] ==  board[3] == mark) or
    (board[7] ==  board[5] ==  board[3] == mark) or
    (board[9] ==  board[5] ==  board[1] == mark))

def board_full(board):
    return ' ' not in board[1:]

def player_input(board, avail, player1, player2):
    if player1 == 'X':
        current_player = player1
    elif player2 == 'X':
        current_player = player2
    else:
        print("Some problem has occured, please contact the developer")
    continue_playing = True
    while continue_playing:
        clear()
        if current_player == player1:
            print("Player 1's Turn")
            next_player = player2
        else:
            print("Player 2's Turn")
            next_player = player1
        print_board(board, avail)
        choice = int(input("\nChoose your next position: (1-9): "))
        place_marker(board, avail, current_player, choice)
        current_player = next_player
        if win_check(board, player1) and win_check(board, player2):
            continue_playing = False
            clear()
            print_board(board, avail)
            print("\nIt's a tie\n")
        elif win_check(board, player1):
            continue_playing = False
            clear()
            print_board(board, avail)
            print("\nPlayer 1 has won the game!\n")
        elif win_check(board, player2):
            continue_playing = False
            clear()
            print_board(board, avail)
            print("\nPlayer 2 has won the game!\n")
        elif board_full(board):
            continue_playing = False
            clear()
            print_board(board, avail)
            print("\nIt's a tie\n")

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# print_board(test_board)
init_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
avail_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print_board(init_board)
player1 = input("Player 1, please pick a marker 'X' or 'O': ")
if player1=='X' or player1=='x':
    player1 = 'X'
    player2 = 'O'
    print("\nPlayer 1 will start first")
    player_input(init_board, avail_board, player1, player2)
elif player1=='O' or player1=='o':
    player2 = 'X'
    player1 = 'O'
    print("\nPlayer 2 will play first")
    player_input(init_board, avail_board, player1, player2)
