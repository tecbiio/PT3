ALGO 1: METHODE HUMAINE

Dans mon algo, on regarde la face verte avec la face blanc au dessus (peut marcher avec d'autres face mais les noms des fonctions etc n'aura plus de sens)

-Requis: avoir tableau (caractères plus facile car mieux visualisable (Couleur1/Couleur2)) dans lequel est indiqué chaque arète/coin
-->Initialisé à la main pour les tests
-Faire liste à partir du tableau grâce à fonction récursive ou composée de boucles qui donne la liste des changements d'arètes à effectuer puis changements de coins à effectuer (2e liste peut etre)
-Faire défiler la liste en faisant les fonctions définies à chaque paramètre entré: ex: Si liste = RG BW OB BR faire les fonctions RG, BW, OB et BR
-Réussir à gérer les cas où le nombre d'actions à effectuer est impair (fonction parité à gérer)



# Fichier Swap.py

Ce fichier est à utiliser dans le but de résoudre le rubik's cube de manière "humaine" à l'aveugle.
Il contient deux fonctions permettant d'échanger la place de 2 cases bien précises

Fonctions:
-

    * SwapEdges : Permet d'échanger la place de 2 cases sur les côtés du cube
    * SwapCorners : Permet d'échanger la place de 2 cases sur les coins du cube
    * Parity : Règle les problèmes liés aux fonctions SwapEdges et SwapCorners si ces fonctions sont effectuées un nombre de fois impair

# Fichiers DeplacementCorners et DeplacementEdges

Ces deux fichier remplissent à peu près le même rôle: pouvoir échanger une case précise avec n'importe quelle autre case. 
Par exemple le fichier Deplacement Edges echange la case qui se situe sur la face du haut, 2e ligne, 3 colonne avec n'importe quelle autre case

Exemple de fonction: WB: Echange la case précédemment citée avec celle sur le bord face Blanche/ face Bleue 