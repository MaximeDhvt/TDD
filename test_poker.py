import unittest
from poker import Card, evaluate_hand
from poker import Deck, deal_hand  # On importe les nouvelles fonctionnalités pour le deck auto

class TestPokerHandEvaluation(unittest.TestCase):
    def test_quinte_flush_royale(self):
        hand = [
            Card("Coeur", "As"),
            Card("Coeur", "Roi"),
            Card("Coeur", "Dame"),
            Card("Coeur", "Valet"),
            Card("Coeur", "10")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Quinte Flush Royale")

    def test_quinte_flush(self):
        hand = [
            Card("Pique", "9"),
            Card("Pique", "8"),
            Card("Pique", "7"),
            Card("Pique", "6"),
            Card("Pique", "5")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Quinte Flush")

    def test_carre(self):
        hand = [
            Card("Coeur", "7"),
            Card("Carreau", "7"),
            Card("Trèfle", "7"),
            Card("Pique", "7"),
            Card("Coeur", "9")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Carré")

    def test_full(self):
        hand = [
            Card("Coeur", "10"),
            Card("Carreau", "10"),
            Card("Trèfle", "10"),
            Card("Pique", "4"),
            Card("Coeur", "4")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Full")

    def test_couleur(self):
        hand = [
            Card("Trèfle", "As"),
            Card("Trèfle", "10"),
            Card("Trèfle", "7"),
            Card("Trèfle", "6"),
            Card("Trèfle", "2")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Couleur")

    def test_quinte(self):
        hand = [
            Card("Coeur", "9"),
            Card("Carreau", "8"),
            Card("Trèfle", "7"),
            Card("Pique", "6"),
            Card("Coeur", "5")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Quinte")

    def test_brelan(self):
        hand = [
            Card("Coeur", "8"),
            Card("Carreau", "8"),
            Card("Trèfle", "8"),
            Card("Pique", "Roi"),
            Card("Coeur", "3")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Brelan")

    def test_deux_paires(self):
        hand = [
            Card("Coeur", "Valet"),
            Card("Carreau", "Valet"),
            Card("Trèfle", "4"),
            Card("Pique", "4"),
            Card("Coeur", "As")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Deux Paires")

    def test_paire(self):
        hand = [
            Card("Coeur", "10"),
            Card("Carreau", "10"),
            Card("Trèfle", "Roi"),
            Card("Pique", "4"),
            Card("Coeur", "3")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Paire")

    def test_carte_haute(self):
        hand = [
            Card("Coeur", "2"),
            Card("Carreau", "5"),
            Card("Trèfle", "9"),
            Card("Pique", "Valet"),
            Card("Coeur", "As")
        ]
        result = evaluate_hand(hand)
        self.assertEqual(result['rank_name'], "Carte Haute")

class TestDeck(unittest.TestCase):
    def test_deck_initialisation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52, "Le deck doit contenir 52 cartes.")

    def test_deal_hand(self):
        deck = Deck()
        hand = deck.deal(5)
        self.assertEqual(len(hand), 5, "Une main doit contenir 5 cartes.")
        self.assertEqual(len(deck.cards), 47, "Le deck doit contenir 47 cartes après distribution.")

    def test_deal_hand_function(self):
        deck = Deck()
        hand = deal_hand(deck)
        self.assertEqual(len(hand), 5, "La fonction deal_hand doit retourner 5 cartes.")
        self.assertEqual(len(deck.cards), 47, "Après deal_hand, le deck doit contenir 47 cartes.")

if __name__ == '__main__':
    unittest.main()
