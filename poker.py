import collections
import random

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

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash((self.suit, self.rank))

class Deck:
    def __init__(self):
        suits = ["Coeur", "Carreau", "Trèfle", "Pique"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = []
        for _ in range(num_cards):
            dealt_cards.append(self.cards.pop())
        return dealt_cards

def evaluate_hand(hand):
    """
    Évalue la main de poker et retourne un dictionnaire contenant :
    - 'rank_value' : valeur numérique pour le type de main
    - 'rank_name'  : nom de la main (ex. "Quinte Flush Royale", "Quinte Flush", "Carré", etc.)
    - 'tiebreaker': liste de valeurs pour départager en cas d'égalité
    """
    # Conversion des rangs en valeurs numériques
    ranks = [RANKS_ORDER[card.rank] for card in hand]
    suits = [card.suit for card in hand]
    ranks.sort()  # du plus petit au plus grand

    # Détection de la couleur (Couleur)
    is_flush = len(set(suits)) == 1

    # Détection de la suite (Quinte)
    is_straight = all(ranks[i] + 1 == ranks[i+1] for i in range(len(ranks)-1))
    # Cas particulier de la quinte basse (A,2,3,4,5)
    if ranks == [2, 3, 4, 5, 14]:
        is_straight = True
        ranks = [1, 2, 3, 4, 5]
        ranks.sort()

    # Comptage des occurrences de chaque rang
    counts = collections.Counter(ranks)
    count_values = sorted(counts.values(), reverse=True)

    # Vérification des combinaisons, par ordre décroissant de force
    if is_flush and is_straight:
        # Quinte Flush Royale : suite de 10 à As
        if max(ranks) == RANKS_ORDER["As"] and min(ranks) == 10:
            return {"rank_value": 10, "rank_name": "Quinte Flush Royale", "tiebreaker": sorted(ranks, reverse=True)}
        else:
            return {"rank_value": 9, "rank_name": "Quinte Flush", "tiebreaker": sorted(ranks, reverse=True)}
    if count_values[0] == 4:
        return {"rank_value": 8, "rank_name": "Carré", "tiebreaker": sorted(counts, key=lambda r: (counts[r], r), reverse=True)}
    if count_values[0] == 3 and count_values[1] == 2:
        return {"rank_value": 7, "rank_name": "Full", "tiebreaker": sorted(counts, key=lambda r: (counts[r], r), reverse=True)}
    if is_flush:
        return {"rank_value": 6, "rank_name": "Couleur", "tiebreaker": sorted(ranks, reverse=True)}
    if is_straight:
        return {"rank_value": 5, "rank_name": "Quinte", "tiebreaker": sorted(ranks, reverse=True)}
    if count_values[0] == 3:
        return {"rank_value": 4, "rank_name": "Brelan", "tiebreaker": sorted(counts, key=lambda r: (counts[r], r), reverse=True)}
    if count_values[0] == 2 and list(counts.values()).count(2) == 2:
        return {"rank_value": 3, "rank_name": "Deux Paires", "tiebreaker": sorted(counts, key=lambda r: (counts[r], r), reverse=True)}
    if count_values[0] == 2:
        return {"rank_value": 2, "rank_name": "Paire", "tiebreaker": sorted(counts, key=lambda r: (counts[r], r), reverse=True)}
    return {"rank_value": 1, "rank_name": "Carte Haute", "tiebreaker": sorted(ranks, reverse=True)}

def deal_hand(deck):
    """Distribue 5 cartes depuis le deck."""
    return deck.deal(5)
