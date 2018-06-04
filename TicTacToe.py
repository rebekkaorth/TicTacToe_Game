# initial empty board
game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

player_one = 1
player_two = 2
current_player = 2
same_player_again = False


# prints the board
def print_board(board):
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')


def take_player_input(player_number):
    number = input("Where to put your token? ")

    if game_board[number] == " ":
        if player_number == 1:
            game_board[number] = "X"
        elif player_number == 2:
            game_board[number] = "O"
        else:
            print("Player Number does not exists")
    else:
        global same_player_again
        same_player_again = True
        print("Place already taken!")


def game_over_test(board):
    for item in board:
        if item == ' ' or item == '#':
            return False
    else:
        return True


def winner(board):
    # criss-cross check
    if board[1] == board[5] and board[1] == board[9]:
        return board[1]
    elif board[3] == board[5] and board[3] == board[7]:
        return board[3]
    # horizontal check
    elif board[1] == board[2] and board[1] == board[3]:
        return board[1]
    elif board[4] == board[5] and board[4] == board[6]:
        return board[4]
    elif board[7] == board[8] and board[7] == board[9]:
        return board[7]
    # vertical check
    elif board[1] == board[4] and board[1] == board[7]:
        return board[1]
    elif board[2] == board[5] and board[2] == board[8]:
        return board[2]
    elif board[3] == board[6] and board[3] == board[9]:
        return board[3]


def get_active_player(active_player):
    global same_player_again
    same_player_again = False
    if active_player == player_one:
        return player_two
    elif active_player == player_two:
        return player_one


def game(board, cur_player):

    print("Please enter numbers between 1 and 9 to place your token!")
    print_board(board)
    while not game_over_test(board):

        if not same_player_again:
            cur_player = get_active_player(cur_player)
        print("\n\r")
        print("It's player " + cur_player.__str__() + "'s turn!")
        print("\n\r")
        take_player_input(cur_player)
        print_board(board)
        if winner(board) == "X":
            print("Player 1 wins!")
            break
        elif winner(board) == "O":
            print("Player 2 wins!")
            break
        print("\n\r")

    print('Game over!')


game(game_board, current_player)
