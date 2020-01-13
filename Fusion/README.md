# Fichier Movement.py

Fichier factorisant les fichiers de mouvements - publique

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
  * initialisation : Place les servomoteurs de tel sorte à ce qu'ils soient correctement initialisés
  * fin : Retire tout les servomoteurs d'enclenchement et de desenclenchement pour pouvoir récupérer le cube
  * pictures : Enchaînement des fonctions x() et y() afin d'acquérir les images du cube

Utilisation de Movement.py :
-

Chaque fonctions permet d'appeler les fonctions relatives au cube virtuel et au cube physique afin de pouvoir contrôler les deux en même temps, c'est le seul qui peut utiliser MovementCube et MovementRobot.  

# Fichier MovementRobot.py

Fichier de mouvements pour un cube physique - privé

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
  * x : Déplace toutes les faces vers la gauche par rapport à la face que l'on regarde
  * y : Déplace toutes les faces vers le bas par rapport à la face que l'on regarde
  * initialisation : Place les servomoteurs de tel sorte à ce qu'ils soient correctement initialisés
  * fin : Retire tout les servomoteurs d'enclenchement et de desenclenchement pour pouvoir récupérer le cube

Utilisation de MovementRobot.py :
-

Les fonctions permettent de contrôler le robot.   

# Fichier MovementCube.py

Fichier de mouvements pour un cube virtuel - privé

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
  * x : déplace toutes les faces vers la gauche par rapport à la face que l'on regarde - pas utilisée
  * y : déplace toutes les faces vers le bas par rapport à la face que l'on regarde - pas utilisée

Système de coordonnées par convention du tableau représentant le cube :
-

Je suis parti dans un système de coordonnées stricte qui respectent une
convention, j'aurai pû faire un système plus flexible mais qui aurait été
beaucoup plus compliqué
(Pour un affichage du cube virtuel par exemple mon cube n'est pas correcte,
car chaque face est définie suivant une face unique au dessus (blanche ou verte ))  

  * Pour les faces 0, 1, 2, 3 -> face blanche (4) au dessus et jaune (5) en dessous
  * Pour les faces 4 et 5 -> face verte (0) au dessus et bleu (2) en dessous

Utilisation de MovementCube.py :
-

Tableau contenant un entier représentant chaque couleur.  
Les fonctions de mouvement, prennent un entier en paramètre qui correspond à la couleur de la face centrale où l'on veut appliquer la fonction.  

# Fichier RubiksCube.py :

Fichier de création d'un cube virtuel - publique

Fonctions :
-

  * __init__ : constructeur du cube qui implique la construction du tableau
  * getTab : getteur du tableau
  * setTab : setteur du tableau avec un tableau
  * getValTab : retourne la valeur des coordonnées spécifiées en paramètre

# Fichier Main.py :

Fichier de test des objets python - publique

# Fichier test.py :

Fichier de test des rotations du cube x et y - publique    
La convention donne un affichage faux mais les coordonnées pour chaque couleurs sont bien respectées.  

# Fichier testrobot.py :

Fichier de test de la synchronisation des différents modules de mouvements - publique
