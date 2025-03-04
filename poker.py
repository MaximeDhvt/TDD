import collections

RANKS_ORDER = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "Valet": 11, "Dame": 12, "Roi": 13, "As": 14
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} de {self.suit}"

def evaluate_hand(hand):
    # Conversion des rangs en valeurs numériques
    ranks = [RANKS_ORDER[card.rank] for card in hand]
    # Comptage des occurrences
    counts = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    # Si une paire est détectée
    if 2 in counts.values():
        return {"rank_value": 2, "rank_name": "Paire", "tiebreaker": sorted(ranks, reverse=True)}
    # Sinon, retourne "Carte Haute"
    return {"rank_value": 1, "rank_name": "Carte Haute", "tiebreaker": sorted(ranks, reverse=True)}
