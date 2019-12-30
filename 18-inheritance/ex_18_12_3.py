# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.18.12 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

from ex_18_12_2 import Hand, Deck


class Hist(dict):
    """A map from each item to its frequency."""

    def __init__(self, seq=None):
        """Creates a new histogram starting with the items in sequence."""
        super().__init__()
        if seq is None:
            seq = []

        for el in seq:
            self.count(el)

    def count(self, item, f=1):
        """Increments the counter associated with item."""
        self[item] = self.get(item, 0) + f
        if self[item] == 0:
            del self[item]


class PokerHand(Hand):
    """Represents a poker hand."""

    labels = ['straight_flush', 'four_of_kind', 'full_house', 'flush',
              'straight', 'three_of_kind', 'two_pair', 'pair', 'high_card']

    def __init__(self):
        super().__init__()
        self.labels = []
        self.suits = Hist()
        self.ranks = Hist()
        self.sets = []

    def make_histograms(self):
        """Computes histograms for suits and ranks."""
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def check_sets(self, *t):
        """Checks whether self.sets contains sets that are
        at least as big as requirements in t.

        :param t: list of int
        """
        for need, have in zip(t, self.sets):
            if need > have:
                return False
        return True

    def has_high_card(self):
        """Returns True if the hand has a high card, False otherwise."""
        return len(self.cards) > 0

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        return self.check_sets(2)

    def has_two_pair(self):
        """Returns True if the hand has a two pair, False otherwise."""
        return self.check_sets(2, 2)

    def has_three_of_kind(self):
        """Returns True if the hand has three cards with the same rank, False otherwise."""
        return self.check_sets(3)

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.

        Straight is a five cards with ranks in sequence.
        """
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)  # aces can be high or low

        return self.ranks_in_a_row(ranks, 5)

    @staticmethod
    def ranks_in_a_row(ranks, n=5):
        """Checks whether the histogram has n ranks in a row.

        :param ranks: map from rank to frequency
        :param n: number we need to get to
        """
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == n:
                    return True
            else:
                count = 0

        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise."""
        return self.check_sets(3, 2)

    def has_four_of_kind(self):
        """Returns True if the hand has four cards with the same rank, False otherwise."""
        self.check_sets(4)

    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise."""
        s = set()
        for c in self.cards:
            s.add((c.rank, c.suit))
            if c.rank == 1:
                s.add((14, c.suit))

        for suit in range(4):
            count = 0
            for rank in range(1, 15):
                if (rank, suit) in s:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0

        return False

    def classify(self):
        """Figures out the classification for the hand."""

        self.make_histograms()
        self.labels = []

        for label in PokerHand.labels:
            has = getattr(self, 'has_'+label)
            if has():
                self.labels.append(label)


class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands."""

    def deal_hands(self, num_hand=7, num_card=7):
        """Creates the hands and deals cards per hand.

         Returns a list of hands.

         :param num_hand: number of Hand objects
         :param num_card: number of cards per hand
         """
        hands = []
        for h in range(num_hand):
            hand = PokerHand()
            self.move_cards(hand, num_card)
            hand.classify()
            hands.append(hand)
        return hands


if __name__ == '__main__':

    # map from label to number of occurrences
    label_hist = Hist()

    num_hand = 7
    num_card = 7

    n = 10000
    for i in range(n):
        if i % 1000 == 0:
            print(i)

        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(num_hand, num_card)
        for hand in hands:
            for label in hand.labels:
                label_hist.count(label)

    # results
    total = num_hand * n
    for label in PokerHand.labels:
        freq = label_hist.get(label, 0)
        p = freq / total
        print('%s happens one time in %.2f' % (label, p))
