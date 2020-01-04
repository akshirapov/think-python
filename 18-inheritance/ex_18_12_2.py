# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.18.12 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import random


class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank."""
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Represents a deck of cards."""

    def __init__(self):
        """Initialises the Deck with 52 cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def pop_card(self):
        """Removes and returns a card from the deck."""
        return self.cards.pop()

    def shuffle(self):
        """Shuffles cards in the deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into hand.

        :param hand: destination Hand object
        :param num: number of cards to move
        """
        for _ in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hand=0, num_card=0):
        """Creates the hands and deals cards per hand.

        Returns a list of hands.

        :param num_hand: number of Hand objects
        :param num_card: number of cards
        """
        hands = []
        for h in range(num_hand):
            hand = Hand(f'Hand #{h}')
            self.move_cards(hand, num_card)
            hands.append(hand)
        return hands


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.label = label
        self.cards = []


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method name if it is invoked on obj.

    :param obj: any python object
    :param method_name: string
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty


def main():
    deck = Deck()
    deck.shuffle()

    hands = deck.deal_hands(2, 2)
    for h in hands:
        print(h.label, end=':\n')
        print(h)


if __name__ == '__main__':
    main()
