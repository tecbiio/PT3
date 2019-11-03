# Fichier Movement.py
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
  * front : Mouvement français officiel A
  * inverseFront : Mouvement français officiel AI
  * behind : Mouvement français officiel P
  * inverseBehind : Mouvement français officiel PI

Système de coordonnées par convention du tableau représentant le cube
-

  * Pour les faces 0, 1, 2, 3 -> face blanche (4) au dessus et jaune (5) en dessous
  * Pour la face 4 -> face verte (0) au dessus et bleu (2) en dessous
  * Pour la face 5 -> face verte (0) au dessus et bleu (2) en dessous

Utilisation de Movement.py :
-

Tableau contenant un entier représentant chaque face de couleur.  
Les fonctions de mouvement, prennent un entier en paramètre qui correspond à la couleur de la face centrale.  

# Fichier RubiksCube.py :
Fonctions
-

  * __init__ : constructeur du cube qui implique la construction du tableau
  * get_tab : getteur du tableau
  * set_tab : setteur du tableau avec un tableau
  * set_val_tab : inclut une valeur au coordonnées spécifiées en paramètre

# Fichier Main.py :

Fichier de test des objets python.

# Fichier TestMovement.py :

Fichier de test avec interface de Movement.  
Plus la combinaisons de fonctions sera grande, plus le test sera significatif.  

# Fichier TestMovement.txt :

Fichier de récupération des tests avec succés.  
Si défaut : remise à zéro après changements dans Movement.py.  
