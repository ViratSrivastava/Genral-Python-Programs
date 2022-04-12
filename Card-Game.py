import random
Suits = ("Hearts", "Diamonds", "Spades", "Clubs")
Ranks = ("Two","Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

Values = {"Two":2,"Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,"Jack":11, "Queen":12, "King":13, "Ace":14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of  " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                Created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

Card_deck =  Deck()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"

Player_one = Player("one")
Player_two = Player("Two")
New_deck = Deck()
New_deck.shuffle()

for x in range(26):
    Player_one.add_cards(new_deck.deal_one())
    Player_two.add_cards(new_deck.deal_one())
Game_on = True
Round_no = 0
while game_on:
Round_no += 1
    print(f”Round number: {round_no}”)
    if len(player_one.all_cards) == 0:
        print("Player 1 out of cards, Player 2 is winner")
Game_on = False
        break
    If len(player_two.all_cards) == 0:
        Print(‘Player 2 out of cards, Player 1 is winner’)
Game_on = False
        Break
Player_one_cards = []
Player_one_cards.append(player_one.remove_one())
Player_two_cards = []
Player_two_cards.append(player_two.remove_one())

At_war = True
    While at_war:
        If player_one_cards[-1].value >player_two_cards[-1].value:
Player_one.add_cards(player_one_cards)
Player_one.add_cards(player_two_cards)
At_war = False
Elifplayer_one_cards[-1].value <player_two_cards[-1].value:

Player_two.add_cards(player_two_cards)
Player_two.add_cards(player_one_cards)
At_war = False

        Else:
            Print(‘War’)
            If len(player_one.all_cards) < 5:
                Print(‘Player 1 has less than 3 cards, Player 2 Wins’)
Game_on = False
                Break

Eliflen(player_two.all_cards) < 5:
                Print(‘Player 2 has less than 3 cards, Player 1 wins’)
Game_on = False
                Break

            Else:
                For num in range(5):
Player_one_cards.append(player_one.remove_one())
Player_two_cards.append(player_two.remove_one())
