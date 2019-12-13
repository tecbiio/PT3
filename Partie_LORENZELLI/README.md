# Fichier Movement.py

Fichier factorisant les fichiers de mouvements

# Fichier MovementRobot.py

Fichier de mouvements pour un cube physique

# Fichier MovementCube.py

Fichier de mouvements pour un cube virtuel

Fonctions :
-

  * right : Mouvement français officiel D
  * inverseRight : Mouvement français officiel DI
  * left : Mouvement français officiel G
  * inverseLeft : Mouvement français officiel GI
  * up : Mouvement français officiel H
  * inverseUp : Mouvement français officiel HI
  * down : Mouvement français officiel B
  * inverseDown : Mouvement français officiel BI

Système de coordonnées par convention du tableau représentant le cube :
-

  * Pour les faces 0, 1, 2, 3 -> face blanche (4) au dessus et jaune (5) en dessous
  * Pour les faces 4 et 5 -> face verte (0) au dessus et bleu (2) en dessous

Utilisation de MovementCube.py :
-

Tableau contenant un entier représentant chaque couleur.  
Les fonctions de mouvement, prennent un entier en paramètre qui correspond à la couleur de la face centrale.  

# Fichier RubiksCube.py :

Fichier de création d'un cube virtuel

Fonctions :
-

  * __init__ : constructeur du cube qui implique la construction du tableau
  * getTab : getteur du tableau
  * setTab : setteur du tableau avec un tableau
  * getValTab : retourne la valeur des coordonnées spécifiées en paramètre

# Fichier Main.py :

Fichier de test des objets python.

# Fichier TestMovement.py :

Fichier de test de Movement avec interface.  
Plus la combinaisons de fonctions est grande, plus le test est significatif.  
