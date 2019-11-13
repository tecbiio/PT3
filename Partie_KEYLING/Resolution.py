import numpy as np
#import DeplacementCorners as dc
import DeplacementEdges as de
import random as r

class Resolution:
    #Création tableau (à récupérer après)
    def main(self):
        tab = array([1,2,3,4,5,6][1,2,3][1,2,3])
        tab[1][1][1]="O"
        tab[1][1][2]="O"
        tab[1][1][3]="R"
        tab[1][2][1]="G"
        tab[1][2][2]="W"
        tab[1][2][3]="R" # 1ère face Position interchangeable
        tab[1][3][1]="W"
        tab[1][3][2]="B"
        tab[1][3][3]="G"
        tab[2][1][1]="W"
        tab[2][1][2]="B"
        tab[2][1][3]="Y"
        tab[2][2][1]="W" # 2nde face Position interchangeable
        tab[2][2][2]="R"
        tab[2][2][3]="B"
        tab[2][3][1]="Y"
        tab[2][3][2]="G"
        tab[2][3][3]="R"
        tab[3][1][1]="R"
        tab[3][1][2]="O"
        tab[3][1][3]="G"
        tab[3][2][1]="W"
        tab[3][2][2]="Y"
        tab[3][2][3]="R"
        tab[3][3][1]="W"
        tab[3][3][2]="O"
        tab[3][3][3]="R"
        tab[4][1][1]="W"
        tab[4][1][2]="Y"
        tab[4][1][3]="Y"
        tab[4][2][1]="B"
        tab[4][2][2]="O"
        tab[4][2][3]="W"
        tab[4][3][1]="B"
        tab[4][3][2]="G"
        tab[4][3][3]="B"
        tab[5][1][1]="O"
        tab[5][1][2]="O"
        tab[5][1][3]="O"
        tab[5][2][1]="Y"
        tab[5][2][2]="G"
        tab[5][2][3]="R"
        tab[5][3][1]="Y"
        tab[5][3][2]="W"
        tab[5][3][3]="B"
        tab[6][1][1]="O"
        tab[6][1][2]="Y"
        tab[6][1][3]="G"
        tab[6][2][1]="R"
        tab[6][2][2]="B"
        tab[6][2][3]="Y"
        tab[6][3][1]="B"
        tab[6][3][2]="G"
        tab[6][3][3]="G"

        #Fin création

        #Modélisation arrêtes / coins

        #           |18|17|16|
        #           |19|B |15|
        #           |01|02|03|
        # |18|19|01| |01|02|03| |03|15|16| |16|17|18|
        # |22|O |04| |04|W |06| |06|R |20| |20|Y |22|
        # |13|14|07| |07|08|09| |09|10|11| |11|12|13|
        #             |07|08|09|
        #             |14|G |10|
        #             |13|12|11|

        #for i in range (1,6):
            #for j in range (1,3):
                #for k in range (1,3):
                    #print(tab[i][j][k])
                
        
        # Boucle plaçant l'arrète ab à sa bonne place
        # PAS OPTIMAL
        # PAS TESTABLE TANT QUE LES FONCTIONS "MOUVEMENT" NE CHANGENT RIEN A MON TABLEAU
        test = 0
        while test == 0:
            a = tab[1][2][3]
            b = tab[2][2][1]
            fonc = a + b
            if fonc == "WR":
                for i in range (1,6):
                    if (tab[i][2][2]==tab[i][2][1]) and (tab[i][2][2]==tab[i][1][2]) and (tab[i][2][2]==tab[i][2][3]) and (tab[i][2][2]==tab[i][3][2]):
                        test = 1
                if test == 0:
                    alea1 = r.randint(1,6)
                    if (alea1 >= 4):
                        if (alea1 == 5) or (alea1 == 6):
                            alea1b = 2
                        else:  
                            alea1b = 1
                    else:
                        alea1b = alea1 + 1
                    
                    
                    alea2 = r.randint(1,2)
                    if alea2 == 2:
                        alea2 = 3
                        alea2b = 1
                    else:
                        alea2b = 3
                    
                    a = tab[alea1][2][alea2]
                    b = tab[alea1b][2][alea2b]
                    fonc = a + b
                        
            de.deplacer(fonc)




