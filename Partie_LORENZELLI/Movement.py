import numpy as np
import RubiksCube

class Movement:

    def rightMovement(self, cube, id):
        tab = cube.get_tab()
        # Face 0, Couleur Vert
        if (id == 0):
            # rotation cote droit
            # sauvegarde cote droit
            tmp1 = tab[0,2,0]
            tmp2 = tab[0,2,1]
            tmp3 = tab[0,2,2]
            # cote droit face 5 sur cote droit face 0
            tab[0,2,0] = tab[5,2,0]
            tab[0,2,1] = tab[5,2,1]
            tab[0,2,2] = tab[5,2,2]
            # cote droit face 2 sur cote droit face 5
            tab[5,2,0] = tab[2,2,0]
            tab[5,2,1] = tab[2,2,1]
            tab[5,2,2] = tab[2,2,2]
            # cote droit face 4 sur cote droit face 2
            tab[2,2,0] = tab[4,2,0]
            tab[2,2,1] = tab[4,2,1]
            tab[2,2,2] = tab[4,2,2]
            # cote droit face 0 sur cote droit face 4
            tab[4,2,0] = tmp1
            tab[4,2,1] = tmp2
            tab[4,2,2] = tmp3
            # rotation de la face 1
            # sauvegarde cote haut face 1
            tmp1 = tab[1,0,0]
            tmp2 = tab[1,1,0]
            tmp3 = tab[1,2,0]
            # cote gauche face 1 sur cote haut face 1
            tab[1,0,0] = tab[1,0,2]
            tab[1,1,0] = tab[1,0,1]
            tab[1,2,0] = tmp1
            # cote bas face 1 sur cote gauche face 1
            tab[1,0,1] = tab[1,1,2]
            tab[1,0,2] = tab[1,2,2]
            # cote droit face 1 sur cote bas face 1
            tab[1,1,2] = tab[1,2,1]
            tab[1,2,2] = tmp3
            # cote droit avec la sauvegarde
            tab[1,2,1] = tmp2
        # Face 1, Couleur Rouge
        # Face 2, Couleur Bleu
        # Face 3, Couleur Orange
        # Face 4, Couleur Blanc
        # Face 5, Couleur Jaune
        return tab
