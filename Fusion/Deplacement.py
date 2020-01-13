'''
FAIT PAR MARTIN KEYLING
Le fichier avait besoin d'être appelé depuis le main et a donc été déplacé

'''
#import Movement as m
import RubiksCube as R 

#Deplacement des arètes pour pouvoir les échanger facilement ": 
#le résultat de chaque fonction va se trouver en position 
#WO pour etre échangé avec celui en position WR
#puis on et la nouvelle arète dans la position où elle était
#(nom de la classe à changer)
#Arètes mises plusieurs fois car dépent de leur orientation (2 orientations donc 2 fonc différentes par arète)
class Deplacement:
    def deplacerEdges(self, cube, fonc):
        if fonc=="RG":
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
        elif fonc=="GR":
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            m.right(Movement,cube,0)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,0)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
        elif fonc=="GO":
            m.left(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invLeft(Movement,cube,0)
        elif fonc=="OG":
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
        elif fonc=="OB":
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,4)
            m.invUp(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.up(Movement,cube,0)
            m.right(Movement,cube,4)
            m.invUp(Movement,cube,0)
        elif fonc=="BO":
            m.invLeft(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.left(Movement,cube,0)
        elif fonc=="BR":
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,0)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            m.right(Movement,cube,0)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
        elif fonc=="RB":
            m.up(Movement,cube,0)
            m.right(Movement,cube,4)
            m.invUp(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,4)
            m.invUp(Movement,cube,0)
        elif fonc=="YR":
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,0)
            m.invRight(Movement,cube,0)
            m.up(Movement,cube,0)
            m.up(Movement,cube,0)        
        elif fonc=="RY":
            m.down(Movement,cube,0)
            m.down(Movement,cube,0)
            m.left(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
            m.invLeft(Movement,cube,0)
            m.down(Movement,cube,0)
            m.down(Movement,cube,0)
        elif fonc=="YG":
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
        elif fonc=="GY":
            m.down(Movement,cube,0)
            m.left(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
            m.invLeft(Movement,cube,0)
            m.invDown(Movement,cube,0)
        elif fonc=="YO":
            m.left(Movement,cube,0)
            m.left(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.left(Movement,cube,0)
            m.left(Movement,cube,0)
        elif fonc=="OY":
            m.left(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
            m.invLeft(Movement,cube,0)
        elif fonc=="YB":
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,4)
            m.invRight(Movement,cube,4)
            m.invUp(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.up(Movement,cube,0)
            m.invRight(Movement,cube,4)
            m.invRight(Movement,cube,4)
            m.invUp(Movement,cube,0)
        elif fonc=="BY":
            m.invDown(Movement,cube,0)
            m.left(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
            m.invLeft(Movement,cube,0)
            m.down(Movement,cube,0)
        elif fonc=="WG":
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            m.up(Movement,cube,0)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
        elif fonc=="GW":
            m.right(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.left(Movement,cube,0)
            m.invRight(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.right(Movement,cube,0)
            m.invLeft(Movement,cube,0)
            m.left(Movement,cube,4)
            m.invRight(Movement,cube,0)
        elif fonc=="WO":
            swapEdges(Deplacement,cube)
        elif fonc=="OW":
            m.invLeft(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.up(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invUp(Movement,cube,0)
            m.left(Movement,cube,4)
            m.up(Movement,cube,0)
            m.left(Movement,cube,0)
        elif fonc=="WB":
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            m.invUp(Movement,cube,0)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            m.up(Movement,cube,0)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
        elif fonc=="BW":
            m.invRight(Movement,cube,0)
            m.invRight(Movement,cube,4)
            m.invLeft(Movement,cube,0)
            m.right(Movement,cube,0)
            swapEdges(Deplacement,cube)
            m.invRight(Movement,cube,0)
            m.left(Movement,cube,0)
            m.right(Movement,cube,4)
            m.right(Movement,cube,0)
    def modifierEdges(self,chaine,fonc): #Permet de mettre à jour le cube en mémoire: remplace l'arrète demandée avec l'arrète placée en position "WR"
        if fonc=="RG":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[16]
            tab[16]=tmp
            tmp=tab[12]
            tab[12]=tab[41]
            tab[41]=tmp
            return tab
        elif fonc=="GR":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[41]
            tab[41]=tmp
            tmp=tab[12]
            tab[12]=tab[16]
            tab[16]=tmp
            return tab
        elif fonc=="GO":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[39]
            tab[39]=tmp
            tmp=tab[12]
            tab[12]=tab[34]
            tab[34]=tmp
            return tab
        elif fonc=="OG":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[34]
            tab[34]=tmp
            tmp=tab[12]
            tab[12]=tab[39]
            tab[39]=tmp
            return tab
        elif fonc=="OB":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[28]
            tab[28]=tmp
            tmp=tab[12]
            tab[12]=tab[48]
            tab[48]=tmp
            return tab
        elif fonc=="BO":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[48]
            tab[48]=tmp
            tmp=tab[12]
            tab[12]=tab[28]
            tab[28]=tmp
            return tab
        elif fonc=="BR":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[50]
            tab[50]=tmp
            tmp=tab[12]
            tab[12]=tab[10]
            tab[10]=tmp
            return tab
        elif fonc=="RB":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[10]
            tab[10]=tmp
            tmp=tab[12]
            tab[12]=tab[50]
            tab[50]=tmp
            return tab
        elif fonc=="YR":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[21]
            tab[21]=tmp
            tmp=tab[12]
            tab[12]=tab[14]
            tab[14]=tmp
            return tab
        elif fonc=="RY":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[14]
            tab[14]=tmp
            tmp=tab[12]
            tab[12]=tab[21]
            tab[21]=tmp
            return tab
        elif fonc=="YG":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[25]
            tab[25]=tmp
            tmp=tab[12]
            tab[12]=tab[43]
            tab[43]=tmp
            return tab
        elif fonc=="GY":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[43]
            tab[43]=tmp
            tmp=tab[12]
            tab[12]=tab[25]
            tab[25]=tmp
            return tab
        elif fonc=="YO":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[23]
            tab[23]=tmp
            tmp=tab[12]
            tab[12]=tab[30]
            tab[30]=tmp
            return tab
        elif fonc=="OY":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[30]
            tab[30]=tmp
            tmp=tab[12]
            tab[12]=tab[23]
            tab[23]=tmp
            return tab
        elif fonc=="YB":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[19]
            tab[19]=tmp
            tmp=tab[12]
            tab[12]=tab[46]
            tab[46]=tmp
            return tab
        elif fonc=="BY":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[46]
            tab[46]=tmp
            tmp=tab[12]
            tab[12]=tab[19]
            tab[19]=tmp
            return tab
        elif fonc=="WG":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[7]
            tab[7]=tmp
            tmp=tab[12]
            tab[12]=tab[37]
            tab[37]=tmp
            return tab
        elif fonc=="GW":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[37]
            tab[37]=tmp
            tmp=tab[12]
            tab[12]=tab[7]
            tab[7]=tmp
            return tab
        elif fonc=="WO":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[3]
            tab[3]=tmp
            tmp=tab[12]
            tab[12]=tab[32]
            tab[32]=tmp
            return tab
        elif fonc=="OW":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[32]
            tab[32]=tmp
            tmp=tab[12]
            tab[12]=tab[3]
            tab[3]=tmp
            return tab
        elif fonc=="WB":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[1]
            tab[1]=tmp
            tmp=tab[12]
            tab[12]=tab[52]
            tab[52]=tmp
            return tab
        elif fonc=="BW":
            tab=list(chaine)
            tmp=tab[5]
            tab[5]=tab[52]
            tab[52]=tmp
            tmp=tab[12]
            tab[12]=tab[1]
            tab[1]=tmp
            return tab

    #Deplacement des coins pour pouvoir les échanger facilement : 
    #le résultat de chaque fonction va se trouver en position 
    #YGR pour etre échangé avec celui en position OBW
    #puis on met le nouveau coin dans la position où il était
    #(nom de la classe à changer)
    #Coins mis plusieurs fois car dépent de leur orientation (3 orientations différentes par coin)
    def deplacerCorners(self,cube,fonc):
        if fonc=="WBR":
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.right(Movement,cube,0)
            m.right(Movement,cube,0)
        elif fonc=="WRG":
            m.invLeft(Movement,cube,4)
            m.invLeft(Movement,cube,4)
            m.invDown(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.down(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            m.invLeft(Movement,cube,4)
        elif fonc=="WGO":
            m.invLeft(Movement,cube,4)
            swapCorners(Deplacement,cube)
            m.invLeft(Movement,cube,4)
        elif fonc=="BOY":
            m.invDown(Movement,cube,0)
            m.left(Movement,cube,4)
            swapCorners(Deplacement,cube)
            m.invLeft(Movement,cube,4)
            m.down(Movement,cube,0)
        elif fonc=="BYR":
            m.right(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invRight(Movement,cube,0)
        elif fonc=="BRW":
            m.right(Movement,cube,0)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
            m.invRight(Movement,cube,0)
        elif fonc=="RBY":
            m.down(Movement,cube,0)
            m.right(Movement,cube,0)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
            m.invRight(Movement,cube,0)
            m.invDown(Movement,cube,0)
        elif fonc=="RYG":
            m.invLeft(Movement,cube,4)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
            m.left(Movement,cube,4)
        elif fonc=="RGW":
            m.invLeft(Movement,cube,4)
            swapCorners(Deplacement,cube)
            m.left(Movement,cube,4)
        elif fonc=="RWB":
            m.invRight(Movement,cube,0)
            m.invLeft(Movement,cube,4)
            swapCorners(Deplacement,cube)
            m.left(Movement,cube,4)
            m.right(Movement,cube,0)
        elif fonc=="GRY":
            m.right(Movement,cube,0)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
            m.invRight(Movement,cube,0)
        elif fonc=="GYO":
            m.left(Movement,cube,4)
            m.right(Movement,cube,0)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
            m.invRight(Movement,cube,0)
            m.invLeft(Movement,cube,4)
        elif fonc=="GOW":
            m.invLeft(Movement,cube,4)
            m.right(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invRight(Movement,cube,0)
            m.left(Movement,cube,4)
        elif fonc=="GWR":
            m.invRight(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.right(Movement,cube,0)
        elif fonc=="OGY":
            m.left(Movement,cube,4)
            swapCorners(Deplacement,cube)
            m.invLeft(Movement,cube,4)
        elif fonc=="OYB":
            m.invDown(Movement,cube,0)
            m.right(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invRight(Movement,cube,0)
            m.down(Movement,cube,0)
        elif fonc=="OWG":
            m.left(Movement,cube,4)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
            m.invLeft(Movement,cube,4)           
        elif fonc=="YBO":
            m.down(Movement,cube,0)
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.down(Movement,cube,0)
            m.down(Movement,cube,0)
        elif fonc=="YOG":
            m.invDown(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.down(Movement,cube,0)
        elif fonc=="YGR":
            swapCorners(Deplacement,cube)
        elif fonc=="YRB":
            m.down(Movement,cube,0)
            swapCorners(Deplacement,cube)
            m.invDown(Movement,cube,0)
    def modifierCorners(self,chaine,fonc):
        if fonc=="WOB":
            tab=list(chaine)
            return tab
        elif fonc=="WBR":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[2]
            tab[2]=tmp
            tmp=tab[51]
            tab[51]=tab[53]
            tab[53]=tmp
            tmp=tab[0]
            tab[0]=tab[9]
            tab[9]=tmp
            return tab
        elif fonc=="WRG":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[8]
            tab[8]=tmp
            tmp=tab[51]
            tab[51]=tab[15]
            tab[15]=tmp
            tmp=tab[0]
            tab[0]=tab[38]
            tab[38]=tmp
            return tab
        elif fonc=="WGO":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[6]
            tab[6]=tmp
            tmp=tab[51]
            tab[51]=tab[36]
            tab[36]=tmp
            tmp=tab[0]
            tab[0]=tab[35]
            tab[35]=tmp
            return tab
        elif fonc=="BOY":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[45]
            tab[45]=tmp
            tmp=tab[51]
            tab[51]=tab[27]
            tab[27]=tmp
            tmp=tab[0]
            tab[0]=tab[20]
            tab[20]=tmp
            return tab
        elif fonc=="BYR":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[47]
            tab[47]=tmp
            tmp=tab[51]
            tab[51]=tab[18]
            tab[18]=tmp
            tmp=tab[0]
            tab[0]=tab[11]
            tab[11]=tmp
            return tab
        elif fonc=="BRW":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[53]
            tab[53]=tmp
            tmp=tab[51]
            tab[51]=tab[9]
            tab[9]=tmp
            tmp=tab[0]
            tab[0]=tab[2]
            tab[2]=tmp
            return tab
        elif fonc=="BWO":
            tab=list(chaine)
            return tab
        elif fonc=="RBY":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[11]
            tab[11]=tmp
            tmp=tab[51]
            tab[51]=tab[47]
            tab[47]=tmp
            tmp=tab[0]
            tab[0]=tab[18]
            tab[18]=tmp
            return tab
        elif fonc=="RYG":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[17]
            tab[17]=tmp
            tmp=tab[51]
            tab[51]=tab[24]
            tab[24]=tmp
            tmp=tab[0]
            tab[0]=tab[44]
            tab[44]=tmp
            return tab
        elif fonc=="RGW":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[15]
            tab[15]=tmp
            tmp=tab[51]
            tab[51]=tab[38]
            tab[38]=tmp
            tmp=tab[0]
            tab[0]=tab[8]
            tab[8]=tmp
            return tab
        elif fonc=="RWB":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[9]
            tab[9]=tmp
            tmp=tab[51]
            tab[51]=tab[2]
            tab[2]=tmp
            tmp=tab[0]
            tab[0]=tab[53]
            tab[53]=tmp
            return tab
        elif fonc=="GRY":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[44]
            tab[44]=tmp
            tmp=tab[51]
            tab[51]=tab[17]
            tab[17]=tmp
            tmp=tab[0]
            tab[0]=tab[24]
            tab[24]=tmp
            return tab
        elif fonc=="GYO":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[42]
            tab[42]=tmp
            tmp=tab[51]
            tab[51]=tab[26]
            tab[26]=tmp
            tmp=tab[0]
            tab[0]=tab[33]
            tab[33]=tmp
            return tab
        elif fonc=="GOW":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[36]
            tab[36]=tmp
            tmp=tab[51]
            tab[51]=tab[35]
            tab[35]=tmp
            tmp=tab[0]
            tab[0]=tab[6]
            tab[6]=tmp
            return tab
        elif fonc=="GWR":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[38]
            tab[38]=tmp
            tmp=tab[51]
            tab[51]=tab[8]
            tab[8]=tmp
            tmp=tab[0]
            tab[0]=tab[15]
            tab[15]=tmp
            return tab
        elif fonc=="OGY":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[33]
            tab[33]=tmp
            tmp=tab[51]
            tab[51]=tab[42]
            tab[42]=tmp
            tmp=tab[0]
            tab[0]=tab[26]
            tab[26]=tmp
            return tab
        elif fonc=="OYB":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[27]
            tab[27]=tmp
            tmp=tab[51]
            tab[51]=tab[20]
            tab[20]=tmp
            tmp=tab[0]
            tab[0]=tab[45]
            tab[45]=tmp
            return tab
        elif fonc=="OBW":
            tab=list(chaine)
            return tab
        elif fonc=="OWG":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[35]
            tab[35]=tmp
            tmp=tab[51]
            tab[51]=tab[6]
            tab[6]=tmp
            tmp=tab[0]
            tab[0]=tab[36]
            tab[36]=tmp
            return tab
        elif fonc=="YBO":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[20]
            tab[20]=tmp
            tmp=tab[51]
            tab[51]=tab[45]
            tab[45]=tmp
            tmp=tab[0]
            tab[0]=tab[27]
            tab[27]=tmp
            return tab
        elif fonc=="YOG":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[26]
            tab[26]=tmp
            tmp=tab[51]
            tab[51]=tab[33]
            tab[33]=tmp
            tmp=tab[0]
            tab[0]=tab[42]
            tab[42]=tmp
            return tab
        elif fonc=="YGR":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[24]
            tab[24]=tmp
            tmp=tab[51]
            tab[51]=tab[44]
            tab[44]=tmp
            tmp=tab[0]
            tab[0]=tab[17]
            tab[17]=tmp
            return tab
        elif fonc=="YRB":
            tab=list(chaine)
            tmp=tab[29]
            tab[29]=tab[18]
            tab[18]=tmp
            tmp=tab[51]
            tab[51]=tab[11]
            tab[11]=tmp
            tmp=tab[0]
            tab[0]=tab[47]
            tab[47]=tmp
            return tab
    #Fonction échangeant deux côtés (avec des coins aussi donc à faire avant les coins)
    def swapEdges(self,cube):
        m.right(Movement,cube,0)
        m.up(Movement,cube,0)
        m.invRight(Movement,cube,0)
        m.invUp(Movement,cube,0) 
        m.invRight(Movement,cube,0) 
        m.invLeft(Movement,cube,4)
        m.right(Movement,cube,0)
        m.right(Movement,cube,0)
        m.invUp(Movement,cube,0) 
        m.invRight(Movement,cube,0) 
        m.invUp(Movement,cube,0) 
        m.right(Movement,cube,0)
        m.up(Movement,cube,0)
        m.invRight(Movement,cube,0)
        m.left(Movement,cube,4)
    #Fonction échangeant deux coins
    def swapCorners(self,cube):
        m.right(Movement,cube,0)
        m.invUp(Movement,cube,0)
        m.invRight(Movement,cube,0)
        m.invUp(Movement,cube,0)
        m.right(Movement,cube,0)
        m.up(Movement,cube,0)
        m.invRight(Movement,cube,0)
        m.left(Movement,cube,4)
        m.right(Movement,cube,0)
        m.up(Movement,cube,0)
        m.invRight(Movement,cube,0)
        m.invUp(Movement,cube,0)
        m.invRight(Movement,cube,0)
        m.invLeft(Movement,cube,4)
        m.right(Movement,cube,0)