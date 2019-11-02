# Fichier Movement.py
Fonctions :
-

  * right : Mouvement français officiel D
  * inverseRight : 3 fois le mouvement right DI
  * left : Mouvement français officiel G
  * inverseLeft : 3 fois le mouvement left GI
  * up : Mouvement français officiel H
  * inverseUp : 3 fois le mouvement up HI
  * down : Mouvement français officiel B
  * inverseDown : 3 fois le mouvement down BI
  * front : à déterminer via une autre fonction A
  * inverseFront : à déterminer via une autre fonction AI
  * behind : à déterminer via une autre fonction P
  * inverseBehind : à déterminer via une autre fonction PI

Système de coordonnées par convention du tableau représentant le cube
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
Fonctions
-

  * __init__ : constructeur du cube qui implique la construction du tableau
  * get_tab : getteur du tableau
  * set_tab : setteur du tableau avec un tableau
  * set_val_tab : inclut une valeur au coordonnées spécifiées en paramètre

# Fichier Main.py :

Fichier de test des objets python. 
Pour tester, il faut modifier ou créer un fichier de test et utiliser les fonctions une par une ou en les combinant entre elles.  
Le squelette de chaque fonction est [Objet Movement].[Fonction à tester]([Objet RubiksCube], [id de la face])  
Je pense faire la phase de test via des combinaisons de fonctions dans le main que je reproduirais sur un RubiksCube afin de m'assurer de la fonctionnalité des fonctions.  
Plus la combinaisons de fonctions sera grande, plus le test sera significatif.
