# Courses: colt_py_bootcamps    269
""" 
# to iterate over our cards we need to add folloing code in the "Deck" class
    # note that, we are not defining our own version of iterator (done above)
        #  we're just using iter() over 'self', so we don't need to define next()
def __iter__(self):
    return iter(self)
"""

from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    # ---------    Defining the ITERATOR    ------------
    def __iter__(self):
        return iter(self.cards)
    # ---------    ITERATOR definition ends    ------------

    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        """
        Return a list of cards dealt
        """
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal

        if count == 0:
            raise ValueError("All cards have been dealt")

        if actual == 1:
            return [self.cards.pop()]

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
    print(card)


# python py_ch9_1_3_eg_iTRTR_DECK.py