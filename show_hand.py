from poker import Deck, deal_hand, evaluate_hand, RANKS_ORDER

# Créez une table pour traduire les valeurs numériques en noms de cartes
RANKS_REVERSE = {value: key for key, value in RANKS_ORDER.items()}

# Dictionnaire d'explications personnalisées pour chaque type de main
explanations = {
    "Carte Haute": "car votre main ne forme aucune combinaison gagnante. La carte la plus élevée détermine la force de votre main.",
    "Paire": "car vous avez une paire, et c'est la valeur de cette paire (avec les cartes secondaires) qui départage votre main.",
    "Deux Paires": "car vous avez deux paires, et la valeur des paires ainsi que la carte restante déterminent votre main.",
    "Brelan": "car vous avez un brelan, c'est-à-dire trois cartes de même valeur, qui prime pour départager les mains similaires.",
    "Quinte": "car vous avez une quinte, c'est-à-dire une suite de cinq cartes consécutives.",
    "Couleur": "car vous avez une couleur, c'est-à-dire cinq cartes de la même couleur (même si elles ne se suivent pas).",
    "Full": "car vous avez un full, combinant un brelan et une paire.",
    "Carré": "car vous avez un carré, c'est-à-dire quatre cartes de même valeur.",
    "Quinte Flush": "car vous avez une quinte flush, c'est-à-dire une suite de cinq cartes de la même couleur.",
    "Quinte Flush Royale": "car vous avez la meilleure main possible, une quinte flush royale."
}

# Création d'un deck, mélange et distribution d'une main de 5 cartes
deck = Deck()
deck.shuffle()
hand = deal_hand(deck)

# Affichage de la main distribuée
print("Main distribuée :")
for card in hand:
    print(card)

# Évaluation de la main
result = evaluate_hand(hand)
explanation = explanations.get(result['rank_name'], "")

# Pour "Carte Haute", vous pouvez ajouter une précision sur la carte la plus élevée
if result['rank_name'] == "Carte Haute":
    highest_value = max(result['tiebreaker'])
    highest_card = RANKS_REVERSE[highest_value]
    explanation += f" Votre carte la plus élevée est {highest_card}."

# Affichage du résultat avec l'explication personnalisée
print("\nRésultat de l'évaluation :")
print(f"{result['rank_name']} : {explanation}")
