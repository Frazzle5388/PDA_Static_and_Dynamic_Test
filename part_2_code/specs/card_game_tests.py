import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 5)
        self.card3 = Card("Diamonds", 8)
        self.cards = [self.card1, self.card2, self.card3]
        self.cardgame = CardGame 

    def test_if_player_has_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self, self.card1))
    
    def test_which_card_has_higher_value(self):
        self.assertEqual(self.card3, self.cardgame.highest_card(self, self.card1, self.card3))
    
    def test_total_card_value(self):
        self.assertEqual("You have a total of 14", self.cardgame.cards_total(self, self.cards))