import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                   'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,'Eight':8,
                 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True


# = - = - = - = - = - = - = - = - = - = - = -
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# = - = - = - = - = - = - = - = - = - = - = -
class Deck:

    def __init__(self):
        self.deck = []  # not passed in, so user could not change it.

        for suit in suits:
            for rank in ranks:
                my_card = Card(suit, rank)
                self.deck.append(my_card)

    def __str__(self):
        deck_coposition = ""

        for card in self.deck:
            deck_coposition += '\n' + card.__str__()

        return ("The Deck has: " + deck_coposition)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# = - = - = - = - = - = - = - = - = - = - = -
# Representation of a Player
class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # from Deck.deal()  --> single Card(rank,suit)
        self.cards.append(card)
        self.value += values[card.rank]

        # track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total Value > 21 == True & we still have an Ace == True
        # then change my Ace to 1 instead of 11.
        while self.value > 21 and self.aces:  # == if self.aces > 0
            self.value -= 10
            self.aces -= 1


# = - = - = - = - = - = - = - = - = - = - = -
class Chips:

    def __init__(self, total=100):
        self.total = total  # Can be set as a default value or passed by a user
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# = - = - = - = - = - = - = - = - = - = - = -
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? \n"))

        except ValueError:
            print("Sorry, pls provide an int.")

        else:
            if chips.bet > chips.total:
                print("Sorry. {} chips is not enough.".format(chips.total))
            else:
                break

# = - = - = - = - = - = - = - = - = - = - = -
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

# = - = - = - = - = - = - = - = - = - = - = -
def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter \"h" or \"s" ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands Dealer's Turn.")
            playing = False

        else:
            print('Pls enter \"h" or \"s" only !')
            continue
        break


# = - = - = - = - = - = - = - = - = - = - = -
def show_some(player, dealer):
    # Show only One of the dealer's cards.
    print("\n Dealer's Hand:")
    print("First card is Hidden!")
    print('', dealer.cards[1])

    # Show all (2 cards) of the Player's hand/card.
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    # Show all the Dealer's cards.
    print("\n Dealer's Hand ", *dealer.cards, sep='\n')

    # Calculate & Display the Value. (e.g. J+K == 20)
    print(f"\n Value of Dealer's hand: {dealer.value}")

    # Show all of a Player's cards:
    print("\n Player's Hand:")

    for card in player.cards:
        print(card)
    # or
    # print("\nPlayer's Hand:", *player.cards, sep='\n ')

    print(f"\n Value of Player's hand: {player.value}")


# = - = - = - = - = - = - = - = - = - = - = -
def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()  # in Chips class


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer & Player tie! PUSH")


# = - = - = - = - = - = - = - = - = - = - = -
while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK. Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this global variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:  # or player_hand.value
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print("\n Player's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand?  y / n \n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break


