
# Courses: colt_py_bootcamps    301, 302, 303

""" 
    Example : Your goal in this assignment will be to add tests to the classes you created in the last section: Card  and Deck . 
                    Try to test that instances have the right structure, and write some tests for the methods. 
                    Use some 'before hooks', and try to test for expected errors as well!

                    Note that the shuffle  method will be difficult to test, since it produces a random output. 
                        Rather than trying to test randomness, you may just want to write some smaller, more straightforward tests. 
                        For instance, you could test that shuffle  doesn't change the size of the deck, or 
                        that the list of cards before the shuffle is in a different order than after the shuffle. 
"""


from card import Card
from deck import Deck

import unittest

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")
    
    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """ repr should return a string of the form 'VALUE of SUIT' """
        self.assertEqual(repr(self.card), "A of Hearts")



class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """ decks should have a cards attribute, which is a list with 52 elements"""
        self.assertTrue(isinstance(self.deck.cards, list)) 
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """ repr should return a string of the form 'Deck of COUNT cards.' """
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")

    def test_count(self):
        """count should return a count of the number of cards in the deck. """
        self.assertEqual(self.deck.count(), 52) 
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """ _deal should deal the number of cards specified, if possible """
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        """ _deal should deal the number of cards left in the deck """
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """ _deal should throw a ValueError if the deck is empty """
        self.deck._deal(self.deck.count())  # dealing all the cards
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_cards(self):
        """ deal_card should deal a single card from the deck """
        card = self.deck.cards[-1]  # not removing, just selecting a card, from the last of the list
        delt_card = self.deck.deal_card()
        # check if the delt_card was the last card
        self.assertEqual(card, delt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """ _deal_hand should deal the number of cards passed into it """
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full """ 
        cards = self.deck.cards[:]  # making a copy of everything using [:]
            # because 'self.deck.cards' points to exact same thing
        self.deck.shuffle_card()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError if the deck is not full """ 
        self.deck._deal(1)  # dealing 1 card to make 51 cards
        with self.assertRaises(ValueError):
            self.deck.shuffle_card()

    
if __name__ == "__main__":
    unittest.main()


#  python py_ch13_2_3_EG_cadeck_tst.py



