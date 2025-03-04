Mini Jeu de Poker en TDD

Ce projet implémente un mini jeu de poker où l'on distribue une main de 5 cartes et l'on évalue cette main selon les règles du poker (ex. Carte Haute, Paire, Deux Paires, Brelan, Quinte, Couleur, Full, Carré, Quinte Flush, Quinte Flush Royale). Le développement a été réalisé en adoptant la méthode TDD (Test-Driven Development).

Fonctionnalités

Gestion des cartes :

Représentation d'une carte avec sa couleur et son rang.

Gestion du deck :

Création d'un deck complet de 52 cartes.
Mélange (shuffle) du deck.
Distribution de mains de 5 cartes.

Évaluation des mains :

Analyse d'une main pour déterminer son classement (Carte Haute, Paire, etc.).
Départage des mains en cas d'égalité grâce à une "justification" basée sur les valeurs des cartes.

Tests unitaires :
Ensemble de tests implémenté avec unittest pour valider chaque fonctionnalité du projet.

Prérequis :
Python 3 (version 3.6 ou ultérieure recommandée)

Pour vérifier que tout fonctionne correctement : python -m unittest discover
Un script d'exemple show_hand.py est fourni pour afficher une main distribuée et son évaluation. : python show_hand.py
