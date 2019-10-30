import numpy as np
from RubiksCube import RubiksCube
from Movement import Movement

# Test constructeur
"""
cube = RubiksCube()
print(cube)
"""

# Test getter
"""
tab2 = cube.get_tab()
print(tab2)
"""

# Test Attribution des valeurs par coordonnées
"""
cube.set_val_tab(0,2,1,5)
print(cube.get_tab())
"""

# Test setter
"""
tab3 = np.zeros((6,3,3))
cube.set_tab(tab3)
print(cube.get_tab())
"""

# Test movement
move = Movement()
print(move)

# Test rightMovement
cube2 = RubiksCube()
move.right(cube2, 0)
move.right(cube2, 1)
move.right(cube2, 0)
move.right(cube2, 1)
print(cube2.get_tab())

# Test rotation d'une face suivant le mouvement right
"""
tab = np.zeros((1,3,3))
tab[0,0,0] = 0
tab[0,0,1] = 1
tab[0,0,2] = 2
tab[0,1,0] = 3
tab[0,1,1] = 4
tab[0,1,2] = 5
tab[0,2,0] = 6
tab[0,2,1] = 7
tab[0,2,2] = 8
print(tab)
tmp1 = tab[0,0,0]
tmp2 = tab[0,0,1]
tmp3 = tab[0,0,2]
# cote gauche face 1 sur cote haut face 1
tab[0,0,1] = tab[0,1,0]
tab[0,0,0] = tab[0,2,0]
tab[0,0,2] = tmp1
# cote bas face 1 sur cote gauche face 1
tab[0,1,0] = tab[0,2,1]
tab[0,2,0] = tab[0,2,2]
# cote droit face 1 sur cote bas face 1
tab[0,2,1] = tab[0,1,2]
tab[0,2,2] = tmp3
# cote droit avec la sauvegarde
tab[0,1,2] = tmp2
print(tab)
"""
