
board_content = ['#','-','-','-','-','-','-','-','-','-']
player1_turn = True



def display_board():
    print(board_content[1] + "|" + board_content[2] + "|" + board_content[3])
    print(board_content[4] + "|" + board_content[5] + "|" + board_content[6])
    print(board_content[7] + "|" + board_content[8] + "|" + board_content[9])

# - = - = - = - = - = - = - = - = - = -


def player_input():
    player1 = ''
    player2 = ''
    x_sign = 'X'
    o_sign = 'O'

    while player1 != x_sign or player1 != o_sign:
        player1 = input("Please pick a marker 'X' or 'O': \n")

        if player1 == x_sign:
            player2 = o_sign
            print("First")
        else:
            player2 = x_sign
            print("Second")


        return (player1, player2)



# - = - = - = - = - = - = - = - = - = -
def marker_place():
    choice = "Wrong Value."
    acceptable_range = range(1,10) # 10 is not included
    within_range = False


    while choice.isdigit() == False or within_range == False:
        choice = input("Place a Number of a Cell (1-9) \n")

        # DIGIT_CHECK:
        if choice.isdigit() == False:
            print("Sorry, that is not a digit.")

        # RANGE_CHECK:
        if choice.isdigit():  # == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("Out of Range (0-10).")

    return int(choice)


# - = - = - = - = - = - = - = - = - = -
def gameon_choice():
    # Can be anything, but a 'Y' or 'N'
    choice = "WRONG"

    # While Choice is not a Digit - repeate a loop
    while choice not in ['Y', 'N']:

        # If we convert here, we'll get an Error of input
        choice = input("Would you like to keep playeing? Y or N:")

        if choice not in ['Y', 'N']:

            print("Pls use Y for Yes & N for No.")

    if choice == 'Y':
        return True
    else:
        return False


# Detect current player mark & put it in a list
def change_board(p1, p2, board_cell):

    if player1_turn:
        board_content[board_cell] = p1
        return False
    else:
        board_content[board_cell] = p2
        return True

# Victory Check:
def victory_check():
    # Horizontal:
    if board_content[1] == board_content[2] and board_content[2] == board_content[3]:
        return True
    elif board_content[4] == board_content[5] and board_content[5] == board_content[6]:
        return True
    elif board_content[7] == board_content[8] and board_content[8] == board_content[9]:
        return True
    # Vertical:
    elif board_content[1] == board_content[4] and board_content[4] == board_content[7]:
        return True
    elif board_content[2] == board_content[5] and board_content[5] == board_content[8]:
        return True
    elif board_content[3] == board_content[6] and board_content[6] == board_content[9]:
        return True
    # Diagonal:
    elif board_content[1] == board_content[5] and board_content[5] == board_content[9]:
        return True
    elif board_content[3] == board_content[5] and board_content[5] == board_content[7]:
        return True
    else:
        return False



# - = - = - = - = - = - = - = - = - = -
# Main Game Logic Scenario:
# - = - = - = - = - = - = - = - = - = -
# Variable for keep playing
game_on = True
victory = False

#Start:
display_board()

# Choose sides:
player1_marker, player2_marker = player_input()
print(f"Player1: {player1_marker} & Player2: {player2_marker} \n")


while game_on:
    # Player choose position
    position = marker_place() #return (1-9)

    # Update List content
    change_board(player1_marker, player2_marker, position)
    display_board()



    # Victory check:
    victory = victory_check()
    player1_turn = victory


    if victory == True:
        if player1_turn:
            print("Player 1 Won - Congrats!")
            break
        else:
            print("Player 2 Won - Congrats!")
            break
    # Still Playing?
    game_on = gameon_choice()

