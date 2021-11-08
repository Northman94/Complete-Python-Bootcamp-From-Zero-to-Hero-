
example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example)

print(example)
# [5, 4, 7, 3, 1, 6, 2]



def shuffle_list(myList):
    shuffle(myList)
    return myList

result = shuffle_list(example)

print(result)
# [7, 1, 5, 4, 2, 3, 6]


# Three Cup Monte:

myList2 = ["  ", " 0 ", "  "]

shuffle_list(myList2)
# [' 0 ', '  ', '  ']

def player_guess():
    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a Numb: 0,  1,  2 \n")

    return int(guess)


myIndex = player_guess()
# Pick a Numb: 0,  1,  2
# 1

print(myIndex)
# 1


def check_guess(myList2, guess):
    if myList2[guess] == " 0 ":
        print("Correct Guess!")
    else:
        print(myList2)
        print("Try again!")


# INITIAL LIST

myList2 = ["  ", " 0 ", "  "]

# SHUFFLE LIST

mixedUp_list = shuffle_list(myList2)

# USER GUESS

guess = player_guess()

# CHECK GUESS

check_guess(mixedUp_list,guess)
# Pick a Numb: 0,  1,  2
# 1
# ['  ', '  ', ' 0 ']
# Try again!