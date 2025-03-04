# poker.py

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} de {self.suit}"

def evaluate_hand(hand):
    # Implémentation minimale pour toujours retourner "Carte Haute"
    return {"rank_value": 1, "rank_name": "Carte Haute", "tiebreaker": []}
