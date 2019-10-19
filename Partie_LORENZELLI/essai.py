import cv2
import numpy as np
# -*- coding: utf-8 -*-

###############
#     2D      #
###############

# Initialisation pour utiliser des tableaux numpy
tab2D = np.zeros((2, 2))
# Remplissage des cases une par une
tab2D[0,0]=1;
tab2D[0,1]=1;
# Remplissage des cases sur une colonne complète
tab2D[1,:]=2;
# Initialisation pour utiliser des tableaux numpy
# Affichage du tableau
print(tab2D)
# Modification d'une case
tab2D[0,1]=5
# Affichage du tableau
print(tab2D)

############

print('---------')

###############
#     3D      #
###############

# Initialisation pour utiliser des tableaux numpy
tab3D = np.zeros((2, 2,3))
# Remplissage des cases une par une
tab3D[0,0,0]=1;
tab3D[0,0,1]=1;
tab3D[0,0,2]=1;
# Remplissage des cases sur une colonne complète
tab3D[1,:,:]=2;
# Initialisation pour utiliser des tableaux numpy
# Affichage du tableau
print(tab3D)

print('---------')

# Modification d'une case
tab3D[0,1,2]=5
# Affichage du tableau
print(tab3D)

#####################

print('---------')

#####################
#     image 3D      #
#####################

# Image binaire
img = tab3D[:,:,1]

cv2.imshow('image', img)
cv2.waitKey(0)

# Image couleur (portée par Z)
img = tab3D

cv2.imshow('image', img)
cv2.waitKey(0)
