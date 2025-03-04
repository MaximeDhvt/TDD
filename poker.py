import collections

# Table de correspondance des rangs
RANKS_ORDER = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "Valet": 11, "Dame": 12, "Roi": 13, "As": 14
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit      # "Coeur", "Carreau", "Trèfle", "Pique"
        self.rank = rank      # "2", "3", …, "10", "Valet", "Dame", "Roi", "As"

    def __repr__(self):
        return f"{self.rank} de {self.suit}"