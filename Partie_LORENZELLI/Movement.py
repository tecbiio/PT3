import numpy as np
import RubiksCube

class Movement:

    def right(self, cube, id):
        tab = cube.get_tab()
        # Face 0, Couleur Vert
        if (id == 0):
            # rotation cote droit
            # sauvegarde cote droit
            tmp1 = tab[0,0,2]
            tmp2 = tab[0,1,2]
            tmp3 = tab[0,2,2]
            # cote droit face 5 sur cote droit face 0
            tab[0,0,2] = tab[5,0,2]
            tab[0,1,2] = tab[5,1,2]
            tab[0,2,2] = tab[5,2,2]
            # cote gauche face 2 sur cote droit face 5
            tab[5,0,2] = tab[2,2,0]
            tab[5,1,2] = tab[2,1,0]
            tab[5,2,2] = tab[2,0,0]
            # cote gauche face 4 sur cote gauche face 2
            tab[2,0,0] = tab[4,0,0]
            tab[2,1,0] = tab[4,1,0]
            tab[2,2,0] = tab[4,2,0]
            # cote droit face 0 sur cote gauche face 4
            tab[4,0,0] = tmp3
            tab[4,1,0] = tmp2
            tab[4,2,0] = tmp1
            # rotation de la face 1
            # sauvegarde cote haut face 1
            tmp1 = tab[1,0,0]
            tmp2 = tab[1,0,1]
            tmp3 = tab[1,0,2]
            # cote gauche face 1 sur cote haut face 1
            tab[1,0,1] = tab[1,1,0]
            tab[1,0,0] = tab[1,2,0]
            tab[1,0,2] = tmp1
            # cote bas face 1 sur cote gauche face 1
            tab[1,1,0] = tab[1,2,1]
            tab[1,2,0] = tab[1,2,2]
            # cote droit face 1 sur cote bas face 1
            tab[1,2,1] = tab[1,1,2]
            tab[1,2,2] = tmp3
            # cote droit avec la sauvegarde
            tab[1,1,2] = tmp2
        # Face 1, Couleur Rouge
        if (id == 1):
            # rotation cote droit
            # sauvegarde cote droit
            tmp1 = tab[1,0,2]
            tmp2 = tab[1,1,2]
            tmp3 = tab[1,2,2]
            # cote bas face 5 sur cote droit face 1
            tab[1,0,2] = tab[5,2,2]
            tab[1,1,2] = tab[5,2,1]
            tab[1,2,2] = tab[5,2,0]
            # cote gauche face 3 sur cote bas face 5
            tab[5,2,0] = tab[3,0,0]
            tab[5,2,1] = tab[3,1,0]
            tab[5,2,2] = tab[3,2,0]
            # cote bas face 4 sur cote gauche face 3
            tab[3,0,0] = tab[4,2,0]
            tab[3,1,0] = tab[4,2,1]
            tab[3,2,0] = tab[4,2,2]
            # cote droit face 1 sur cote bas face 4
            tab[4,2,0] = tmp3
            tab[4,2,1] = tmp2
            tab[4,2,2] = tmp1
            # rotation de la face 2
            # sauvegarde cote haut face 2
            tmp1 = tab[2,0,0]
            tmp2 = tab[2,0,1]
            tmp3 = tab[2,0,2]
            # cote gauche face 1 sur cote haut face 1
            tab[2,0,1] = tab[2,1,0]
            tab[2,0,0] = tab[2,2,0]
            tab[2,0,2] = tmp1
            # cote bas face 1 sur cote gauche face 1
            tab[2,1,0] = tab[2,2,1]
            tab[2,2,0] = tab[2,2,2]
            # cote droit face 1 sur cote bas face 1
            tab[2,2,1] = tab[2,1,2]
            tab[2,2,2] = tmp3
            # cote droit avec la sauvegarde
            tab[2,1,2] = tmp2
        # Face 2, Couleur Bleu
        if (id == 2):
            # rotation cote droit
            # sauvegarde cote droit
            tmp1 = tab[2,0,2]
            tmp2 = tab[2,0,2]
            tmp3 = tab[2,0,2]
            # cote gauche face 5 sur cote droit face 2
            tab[2,2,2] = tab[5,0,0]
            tab[2,1,2] = tab[5,1,0]
            tab[2,0,2] = tab[5,2,0]
            # cote gauche face 0 sur cote gauche face 5
            tab[5,0,0] = tab[0,0,0]
            tab[5,1,0] = tab[0,1,0]
            tab[5,2,0] = tab[0,2,0]
            # cote droit face 4 sur cote gauche face 0
            tab[0,2,0] = tab[4,0,2]
            tab[0,1,0] = tab[4,1,2]
            tab[0,0,0] = tab[4,2,2]
            # cote droit face 2 sur cote droit face 4
            tab[4,0,2] = tmp1
            tab[4,1,2] = tmp2
            tab[4,2,2] = tmp3
            # rotation de la face 3
            # sauvegarde cote haut face 3
            tmp1 = tab[3,0,0]
            tmp2 = tab[3,0,1]
            tmp3 = tab[3,0,2]
            # cote gauche face 3 sur cote haut face 3
            tab[3,0,1] = tab[3,1,0]
            tab[3,0,0] = tab[3,2,0]
            tab[3,0,2] = tmp1
            # cote bas face 3 sur cote gauche face 3
            tab[3,1,0] = tab[3,2,1]
            tab[3,2,0] = tab[3,2,2]
            # cote droit face 1 sur cote bas face 3
            tab[3,2,1] = tab[3,1,2]
            tab[3,2,2] = tmp3
            # cote droit avec la sauvegarde
            tab[3,1,2] = tmp2
        # Face 3, Couleur Orange
        if (id == 3):
            # rotation cote droit
            # sauvegarde cote droit
            tmp1 = tab[3,0,2]
            tmp2 = tab[3,1,2]
            tmp3 = tab[3,2,2]
            # cote haut face 5 sur cote droit face 3
            tab[3,0,2] = tab[5,0,0]
            tab[3,1,2] = tab[5,0,1]
            tab[3,2,2] = tab[5,0,2]
            # cote gauche face 1 sur cote haut face 5
            tab[5,0,2] = tab[1,0,0]
            tab[5,0,1] = tab[1,1,0]
            tab[5,0,0] = tab[1,2,0]
            # cote haut face 4 sur cote gauche face 1
            tab[1,2,0] = tab[4,0,0]
            tab[1,1,0] = tab[4,0,1]
            tab[1,0,0] = tab[4,0,2]
            # cote droit face 3 sur cote haut face 4
            tab[4,0,0] = tmp1
            tab[4,0,1] = tmp2
            tab[4,0,2] = tmp3
            # rotation de la face 0
            # sauvegarde cote haut face 0
            tmp1 = tab[0,0,0]
            tmp2 = tab[0,0,1]
            tmp3 = tab[0,0,2]
            # cote gauche face 0 sur cote haut face 0
            tab[0,0,1] = tab[0,1,0]
            tab[0,0,0] = tab[0,2,0]
            tab[0,0,2] = tmp1
            # cote bas face 0 sur cote gauche face 0
            tab[0,1,0] = tab[0,2,1]
            tab[0,2,0] = tab[0,2,2]
            # cote droit face 0 sur cote bas face 0
            tab[0,2,1] = tab[0,1,2]
            tab[0,2,2] = tmp3
            # cote droit avec la sauvegarde
            tab[0,1,2] = tmp2
        # Face 4, Couleur Blanc
        if (id == 4):
            self.right(cube, 2)
        # Face 5, Couleur Jaune
        if (id == 5):
            self.right(cube, 0)

    def inverseRight(self, cube, id):
        for i in range(0,3):
            self.right(cube, id)
