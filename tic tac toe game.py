def display_board():
    if len(board)==10:
        print(board[7]+'|'+board[8]+'|'+ board[9]+'|')
        print('------')
        print(board[4]+'|'+board[5]+'|'+ board[6]+'|')
        print('------')
        print(board[1]+'|'+board[2]+'|'+ board[3]+'|')
board = [' ']*10
display_board()
def player_choice():
    marker = ' '
    while marker not in ['X', 'O']:
        marker = input('choose a marker X or O: ')
    player1 = marker
    if player1 == 'X':
            return ('X', 'O')
    else:
            return ('O', 'X')
def position_choice():
    choice = 'wrong'
    valid_range = range(1,10)
    while True:
        choice = input("enter a position(1-9): ")
        if choice.isdigit():
            choice = int(choice)
            if choice in valid_range:
                break
            else:
                print('sorry, it is invalid')
        else:
            print('sorry, it is invalid')
    return choice
def place_marker(board, marker, position):
    board[position] = marker
def win_game(board, mark):
    win_conditions = [
        [board[7], board[8], board[9]],  
        [board[4], board[5], board[6]],  
        [board[1], board[2], board[3]], 
        [board[7], board[4], board[1]],  
        [board[8], board[5], board[2]],  
        [board[9], board[6], board[3]],  
        [board[7], board[5], board[3]],  
        [board[9], board[5], board[1]]  
    ]
    return [mark, mark, mark] in win_conditions
def full_board_check(board):
    return ' ' not in board[1:]
def replay():
    return input("do you want play aggain? enter yes or no")
print("welcome to tic tac toe!")
while True:
    board = [' ']*10
    player1_marker, player2_marker = player_choice()
    turn = 'player1'
    game_on = True
    while game_on:
        if turn == 'player1':
            display_board()
            position = position_choice()
            place_marker(board, player1_marker, position)
            if win_game(board, player1_marker):
                display_board()
                print("congrats! player1 has won the game!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board()
                    print('the game is draw!')
                    break
                else:
                    turn = 'player2'
        else:
            display_board()
            position = position_choice()
            place_marker(board, player2_marker, position)

            if win_game(board, player2_marker):
                display_board()
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board()
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break




        

