import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 5)
        self.card3 = Card("Diamonds", 8)

    def test_if_card_value_is_one(self):
        self.assertEqual(True, self.card1.value == 1)

    def test_which_card_has_higher_value(self):
        self.assertEqual(1 < 5, self.card1.value < self.card2.value)

    def test_total_card_value(self):
        self.assertEqual(14, self.card1.value + self.card2.value + self.card3.value) 
    