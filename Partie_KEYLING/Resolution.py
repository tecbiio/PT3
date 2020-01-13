from Deplacement import *
import random as r



        #Modélisation arrêtes / coins

        #           |O|Y|G|
        #           |R|B|Y|
        #           |B|G|G|
        # |W|Y|Y| |O|O|R| |W|B|Y| |R|O|G|
        # |B|O|W| |G|W|R| |W|R|B| |W|Y|R|
        # |B|G|B| |W|B|G| |Y|G|R| |W|O|R|
        #             |O|O|O|
        #             |Y|G|R|
        #             |Y|W|B|
    
cube="OORGWRWBGWBYWRBYGRROGWYRWORWYYBOWBGBOOOYGRYWBOYGRBYBGG" #Exemple de String reçue
compteur=0 #Nombre de fonctions à effectuer (savoir le temps de résolution)

#AFFICHAGE CUBE A RESOUDRE
for i in cube:
    print(i,end=" ")
print("")

#RESOLUTION ARRETES

pos_echangeable_bord_1= cube[5]
pos_echangeable_bord_2= cube[12]

cube_init=cube #Sauvegarde le cube initial (sert pour la parité)
test = 0
pos_echangeable_bord_1= cube[5]
pos_echangeable_bord_2= cube[12]
pos_echangeable_bord = pos_echangeable_bord_1+pos_echangeable_bord_2
while test != 5:
    test=0
    if pos_echangeable_bord == "WR" or pos_echangeable_bord == "RW": #Test Résolution bords (Le cube devant être échangé est bien placé)    
        for i in range (0,5):  #On vérifie alors si le cube est résolu : Pour chaque centre on regarde si tous les bords sont bien placés
            if (cube[i*9+4]==cube[i*9+1]) and (cube[i*9+4]==cube[i*9+3]) and (cube[i*9+4]==cube[i*9+5]) and (cube[i*9+4]==cube[i*9+7]):
                test = test + 1
        if test != 5:
            pos_echangeable_bord_1="0"
            pos_echangeable_bord_2="0"
            while pos_echangeable_bord_1==pos_echangeable_bord_2: # Si le cube n'est pas résolu, on change alors ce bord avec un aléatoire
                alea1=r.randint(0,5)
                alea2=r.randint(0,5)
                if alea1==0:
                    pos_echangeable_bord_1="W"
                if alea2==0:
                    pos_echangeable_bord_2="W"
                if alea1==1:
                    pos_echangeable_bord_1="R"
                if alea2==1:
                    pos_echangeable_bord_2="R"
                if alea1==2:
                    pos_echangeable_bord_1="Y"
                if alea2==2:
                    pos_echangeable_bord_2="Y"
                if alea1==3:
                    pos_echangeable_bord_1="O"
                if alea2==3:
                    pos_echangeable_bord_2="O"
                if alea1==4:
                    pos_echangeable_bord_1="G"
                if alea2==4:
                    pos_echangeable_bord_2="G"
                if alea1==5:
                    pos_echangeable_bord_1="B"
                if alea2==5:
                    pos_echangeable_bord_2="B"
                if pos_echangeable_bord_1=="W" and pos_echangeable_bord_2=="R" or pos_echangeable_bord_1=="R" and pos_echangeable_bord_2=="W": #Teste si position ne change pas
                    pos_echangeable_bord_1="0"
                    pos_echangeable_bord_2="0"
                if pos_echangeable_bord_1=="W" and pos_echangeable_bord_2=="Y" or pos_echangeable_bord_1=="Y" and pos_echangeable_bord_2=="W" or pos_echangeable_bord_1=="B" and pos_echangeable_bord_2=="G" or pos_echangeable_bord_1=="G" and pos_echangeable_bord_2=="B" or pos_echangeable_bord_1=="O" and pos_echangeable_bord_2=="R" or pos_echangeable_bord_1=="R" and pos_echangeable_bord_2=="O":#Teste si la position demandée est possible (par exemple, pas de lien entre la couleur blanche et la couleur jaune)
                    pos_echangeable_bord_1="0"
                    pos_echangeable_bord_2="0" 
            pos_echangeable_bord = pos_echangeable_bord_1+pos_echangeable_bord_2           
    else:
        '''Deplacement.deplacerEdges(Deplacement,cube2,pos_echangeable_bord)'''#Déplace le cube
        cube= Deplacement.modifierEdges(Deplacement,cube,pos_echangeable_bord) #Modifie le cube en échangeant l'arrète pos_echangeable_bord avec l'arrète placée en position "WR"
        #Les fonction Deplacement.swapEdges et Deplacement.swapCorners inversent deux cubes à côté d'eux, il faut le prendre en compte aussi
        tmp=cube[2]
        cube[2]=cube[8]
        cube[8]=tmp
        tmp=cube[53]
        cube[53]=cube[15]
        cube[15]=tmp
        tmp=cube[9]
        cube[9]=cube[38]
        cube[38]=tmp
        pos_echangeable_bord = cube[5]+cube[12] #Nouvelle arrète en position "WR"
        compteur=compteur+1

        

#AFFICHAGE ARRETES RESOLUES    
for i in cube:
    print(i,end=" ")
print("")
print(compteur)

#RESOLUTION COINS
pos_echangeable_bord_1=cube[29]
pos_echangeable_bord_2=cube[51]
pos_echangeable_bord_3=cube[0]
pos_echangeable_bord = pos_echangeable_bord_1+pos_echangeable_bord_2+pos_echangeable_bord_3
test=0
while test != 5:
    test=0
    if pos_echangeable_bord == "OBW" or pos_echangeable_bord == "WOB" or pos_echangeable_bord == "BWO": #Test Résolution coins (Le cube devant être échangé est bien placé)    
        for i in range (0,5):  #On vérifie alors si le cube est résolu : Pour chaque centre on regarde si tous les coins sont bien placés
            if (cube[i*9+4]==cube[i*9]) and (cube[i*9+4]==cube[i*9+2]) and (cube[i*9+4]==cube[i*9+6]) and (cube[i*9+4]==cube[i*9+8]):
                test = test + 1
        if test != 5:
            pos_echangeable_bord_1="0"
            pos_echangeable_bord_2="0"
            pos_echangeable_bord_3="0"
            while pos_echangeable_bord_1==pos_echangeable_bord_2 or pos_echangeable_bord_1==pos_echangeable_bord_3 or pos_echangeable_bord_2==pos_echangeable_bord_3: # Si le cube n'est pas résolu, on change alors ce coin avec un aléatoire
                alea1=r.randint(0,5)
                alea2=r.randint(0,5)
                alea3=r.randint(0,5)
                if alea1==0:
                    pos_echangeable_bord_1="W"
                if alea2==0:
                    pos_echangeable_bord_2="W"
                if alea3==0:
                    pos_echangeable_bord_3="W"
                if alea1==1:
                    pos_echangeable_bord_1="R"
                if alea2==1:
                    pos_echangeable_bord_2="R"
                if alea3==1:
                    pos_echangeable_bord_3="R"
                if alea1==2:
                    pos_echangeable_bord_1="Y"
                if alea2==2:
                    pos_echangeable_bord_2="Y"
                if alea3==2:
                    pos_echangeable_bord_3="Y"
                if alea1==3:
                    pos_echangeable_bord_1="O"
                if alea2==3:
                    pos_echangeable_bord_2="O"
                if alea3==3:
                    pos_echangeable_bord_3="O"
                if alea1==4:
                    pos_echangeable_bord_1="G"
                if alea2==4:
                    pos_echangeable_bord_2="G"
                if alea3==4:
                    pos_echangeable_bord_3="G"
                if alea1==5:
                    pos_echangeable_bord_1="B"
                if alea2==5:
                    pos_echangeable_bord_2="B"
                if alea3==5:
                    pos_echangeable_bord_3="B"
                ##Test différent qu'avec les arrètes: les coins sont définis dans seulement un ordre, il faut donc empêcher la création d'un ordre différent##
                if pos_echangeable_bord_1=="B" and pos_echangeable_bord_2=="R" and pos_echangeable_bord_3=="W" or pos_echangeable_bord_1=="W" and pos_echangeable_bord_2=="B" and pos_echangeable_bord_3=="R" or pos_echangeable_bord_1=="R" and pos_echangeable_bord_2=="W" and pos_echangeable_bord_3=="B" or pos_echangeable_bord_1=="B" and pos_echangeable_bord_2=="Y" and pos_echangeable_bord_3=="R" or pos_echangeable_bord_1=="R" and pos_echangeable_bord_2=="B" and pos_echangeable_bord_3=="Y" or pos_echangeable_bord_1=="Y" and pos_echangeable_bord_2=="R" and pos_echangeable_bord_3=="B" or pos_echangeable_bord_1=="B" and pos_echangeable_bord_2=="W" and pos_echangeable_bord_3=="O" or pos_echangeable_bord_1=="O" and pos_echangeable_bord_2=="B" and pos_echangeable_bord_3=="W" or pos_echangeable_bord_1=="W" and pos_echangeable_bord_2=="O" and pos_echangeable_bord_3=="B" or pos_echangeable_bord_1=="B" and pos_echangeable_bord_2=="O" and pos_echangeable_bord_3=="Y" or pos_echangeable_bord_1=="Y" and pos_echangeable_bord_2=="B" and pos_echangeable_bord_3=="O" or pos_echangeable_bord_1=="O" and pos_echangeable_bord_2=="Y" and pos_echangeable_bord_3=="B" or pos_echangeable_bord_1=="G" and pos_echangeable_bord_2=="R" and pos_echangeable_bord_3=="Y" or pos_echangeable_bord_1=="R" and pos_echangeable_bord_2=="Y" and pos_echangeable_bord_3=="G" or pos_echangeable_bord_1=="Y" and pos_echangeable_bord_2=="G" and pos_echangeable_bord_3=="R" or pos_echangeable_bord_1=="G" and pos_echangeable_bord_2=="Y" and pos_echangeable_bord_3=="O" or pos_echangeable_bord_1=="Y" and pos_echangeable_bord_2=="O" and pos_echangeable_bord_3=="G" or pos_echangeable_bord_1=="O" and pos_echangeable_bord_2=="G" and pos_echangeable_bord_3=="Y" or pos_echangeable_bord_1=="G" and pos_echangeable_bord_2=="W" and pos_echangeable_bord_3=="R" or pos_echangeable_bord_1=="W" and pos_echangeable_bord_2=="R" and pos_echangeable_bord_3=="G" or pos_echangeable_bord_1=="R" and pos_echangeable_bord_2=="G" and pos_echangeable_bord_3=="W" or pos_echangeable_bord_1=="G" and pos_echangeable_bord_2=="O" and pos_echangeable_bord_3=="W" or pos_echangeable_bord_1=="O" and pos_echangeable_bord_2=="N" and pos_echangeable_bord_3=="G" or pos_echangeable_bord_1=="N" and pos_echangeable_bord_2=="G" and pos_echangeable_bord_3=="O":
                    pos_echangeable_bord = pos_echangeable_bord_1+pos_echangeable_bord_2+pos_echangeable_bord_3
                else:
                    pos_echangeable_bord_1="0"
                    pos_echangeable_bord_2="0"
                    pos_echangeable_bord_3="0"
    else:
        '''Deplacement.deplacerCorners(Deplacement,cube2,pos_echangeable_bord)'''#Tourne le cube
        cube= Deplacement.modifierCorners(Deplacement,cube,pos_echangeable_bord) #Modifie le cube en échangeant l'arrète pos_echangeable_bord avec l'arrète placée en position "WR"
        #Les fonction Deplacement.swapEdges et Deplacement.swapCorners inversent deux cubes à côté d'eux, il faut le prendre en compte aussi
        tmp=cube[1]
        cube[1]=cube[3]
        cube[3]=tmp
        tmp=cube[52]
        cube[52]=cube[32]
        cube[32]=tmp
        pos_echangeable_bord = cube[29]+cube[51]+cube[0] #Nouveau coin en position "OBW"
        compteur=compteur+1


#AFFICHAGE CUBE RESOLU
for i in cube:
    print(i, end=" ")
print("")
print(compteur)