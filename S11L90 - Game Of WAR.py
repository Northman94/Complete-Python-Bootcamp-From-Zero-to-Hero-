'''
# If I write:
from random import shuffle

# I can use:
shuffle(my_list2)

# But as we do:
import random

# We use:
random.shuffle(my_list2)
'''

import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
                 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]  # Numb

    def __str__(self):
        return self.rank + ' of ' + self.suit


'''
two_hearts = Card("Two","Hearts")
print(two_hearts)

values[two_hearts.rank]

three_of_clubs = Card("Three","Clubs")

two_hearts.value < three_of_clubs.value
'''


# Deck Class:
# Instantiate a new Deck:
# Create all 52 Card Obj-s
# Hold as a List of Card Obj-s Shuffle a Deck through a method call:
# Random Library Shuffle() function Deal Cards from the Deck Obj-s
# Pop method from cards List
# Deck Class will return Card Class instances.

class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a Card Obj
                created_card = Card(rank, suit)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):  # Pick One
        return self.all_cards.pop()



deck_obj = Deck()



for i in deck_obj.all_cards:
    print(i)

print("\n")

deck_obj.shuffle()

for z in deck_obj.all_cards:
    print(z)


'''
my_card = deck_obj.deal_one()
# print(my_card)
# len(deck_obj.all_cards)
'''


#     Player Class:
# Class to hold player's current List of Cards.
# + Should be able to remove/add card Obj-s from List
# + Translate a Deck/Hand of cards with a top/bottom to a List.

class Player():

    def __init__(self, name):
        self.name = name
        self.card_lst = []

    def remove_one(self):
        return self.card_lst.pop(0)

    def add_cards(self, new_cards):
        # if it's a List. (Of Obj-s)
        if type(new_cards) == type([]):
            # Like append, but for more tham 1 Obj:
            self.card_lst.extend(new_cards)
        else:
            # if a single Card Obj.
            self.card_lst.append(new_cards)

    def __str__(self):
        return (f"Player {self.name} has {len(self.card_lst)} cards. \n")


'''
new_player = Player("Jose")
print(new_player)

new_player.add_cards(my_card)
print(my_card)
print(new_player)
print(new_player.remove_one())
'''


# Game Logiс:

player_one = Player("First")
player_two = Player("Second")

new_deck = Deck()
new_deck.shuffle()

# Split Deck between players:
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


'''
len(player_one.card_lst)
# 26
len(player_two.card_lst)
# 26
'''

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f"Round - {round_num}.\n")

    # Player out of Cards check.
    if len(player_one.card_lst) == 0:
        print("Player 1 - Out of Cards. Player 2 Wins")
        game_on = False
        break

    if len(player_two.card_lst) == 0:
        print("Player 2 - Out of Cards. Player 1 Wins")
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False


        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False


        else:
            print("WAR!")

            if len(player_one.card_lst) < 3:
                print("P1 can't declare WAR.")
                print("P2 - WINS!")
                game_on = False
                break  # while at_war

            elif len(player_two.card_lst) < 3:
                print("P2 can't declare WAR.")
                print("P1 - WINS!")
                game_on = False
                break  # while at_war

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

