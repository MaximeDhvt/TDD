import unittest
from poker import Card, evaluate_hand

class TestPokerHandEvaluation(unittest.TestCase):
    def test_carte_haute(self):
        # Carte Haute : aucune combinaison, la carte la plus haute est As
        hand = [
            Card("Coeur", "2"),
            Card("Carreau", "5"),
            Card("Trèfle", "9"),
            Card("Pique", "Valet"),
            Card("Coeur", "As")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Carte Haute")

    def test_paire(self):
        # Paire : une paire de 10, avec trois autres cartes
        hand = [
            Card("Coeur", "10"),
            Card("Carreau", "10"),
            Card("Trèfle", "Roi"),
            Card("Pique", "4"),
            Card("Coeur", "3")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Paire")

if __name__ == '__main__':
    unittest.main()
