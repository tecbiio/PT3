# Fichier Movement.py
Fonctions :
-

  * right : Mouvement français officiel D
  * inverseRight : 3 fois le mouvement right
  * left : Mouvement français officiel G
  * inverseLeft : 3 fois le mouvement left
  * up : Mouvement français officiel H
  * inverseUp : 3 fois le mouvement up
  * down : Mouvement français officiel B
  * inverseDown : 3 fois le mouvement down

Système de coordonnées du tableau représentant le cube
-

  * Pour les faces 0, 1, 2, 3 -> face blanche (4) au dessus et jaune (5) en dessous
  * Pour la face 4 -> face verte (0) en dessous et bleu (2) au dessus
  * Pour la face 5 -> face verte (0) au dessus et bleu (2) en dessous

Utilisation de Movement.py :
-

Tableau contenant un entier représentant chaque face de couleur.
Les fonctions de mouvement, prennent un entier en paramètre qui correspond à la couleur de la face centrale.
Seule la fonction rightMovement pour id = {0,1,2,3} est opérationnelle

# Fichier RubiksCube.py :

Création du tableau propre au cube avec les getteurs et setteurs

# Fichier Main.py :

Fichier de test des objets python
