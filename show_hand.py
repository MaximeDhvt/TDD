from poker import Deck, deal_hand, evaluate_hand

# Créez un deck et mélangez-le
deck = Deck()
deck.shuffle()

# Distribuez une main de 5 cartes
hand = deal_hand(deck)

# Affichez la main distribuée
print("Main distribuée :")
for card in hand:
    print(card)

# Évaluez la main et affichez le résultat
result = evaluate_hand(hand)
print("\nRésultat de l'évaluation :")
print(result)
