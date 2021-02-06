import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("clubs", 7)
     
    def test_card_game_can_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_1))
    
    def test_card_game_can_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_2))

    def test_card_game_can_return_highest_card_1(self):
        self.assertEqual(self.card_2, self.card_game.highest_card(self.card_1, self.card_2))
    
    def test_card_game_can_return_highest_card_2(self):
        self.assertEqual(self.card_2, self.card_game.highest_card(self.card_2, self.card_1))
    
    def test_card_game_can_return_string_total(self):
        test_cards = [self.card_1, self.card_2]
        self.assertEqual("You have a total of 8", self.card_game.cards_total(test_cards))