import Movement as m
import Swap as s

#Deplacement des arètes pour pouvoir les échanger facilement : 
#le résultat de chaque fonction va se trouver en position 
#WO pour etre échangé avec celui en position WR
#puis on met la nouvelle arète dans la position où elle était
#(nom de la classe à changer)
#Arètes mises plusieurs fois car dépent de leur orientation (2 orientations différentes par arète)
class DeplacementEdges:
    def RG():
        m.inverseUpMovement()
        m.inverseFrontMovement()
        m.UpMovement()
        s.swapEdges()
        m.inverseUpMovement()
        m.frontMovement()
        m.upMovement()
    def GR():
        m.upMovement()
        m.upMovement()
        m.rightMovement()
        m.upMovement()
        m.upMovement()
        s.swapEdges()
        m.upMovement()
        m.upMovement()
        m.inverseRightMovement()
        m.upMovement()
        m.upMovement()
    def GO():
        m.leftMovement()
        s.swapEdges()
        m.inverseLeftMovement()
    def OG():
        m.inverseUpMovement()
        m.frontMovement()
        m.upMovement()
        s.swapEdges()
        m.inverseUpMovement()
        m.inverseFrontMovement()
        m.upMovement()
    def OB():
        m.upMovement()
        m.behindMovement()
        m.inverseUpMovement()
        s.swapEdges()
        m.upMovement()
        m.inverseBehindMovement()
        m.inverseUpMovement()
    def BO():
        m.inverseLeftMovement()
        s.swapEdges()
        m.leftMovement()
    def BR():
        m.upMovement()
        m.upMovement()
        m.inverseRightMovement()
        m.upMovement()
        m.upMovement()
        s.swapEdges()
        m.upMovement()
        m.upMovement()
        m.rightMovement()
        m.upMovement()
        m.upMovement()
    def RB():
        m.upMovement()
        m.inverseBehindMovement()
        m.inverseUpMovement()
        s.swapEdges()
        m.upMovement()
        m.behindMovement()
        m.inverseUpMovement()
    def YR():
        m.upMovement()
        m.upMovement()
        m.rightMovement()
        m.rightMovement()
        m.upMovement()
        m.upMovement()
        s.swapEdges()
        m.upMovement()
        m.upMovement()
        m.inverseRightMovement()
        m.inverseRightMovement()
        m.upMovement()
        m.upMovement()        
    def RY():

    def YG():
        m.inverseUpMovement()
        m.frontMovement()
        m.frontMovement()
        m.upMovement()
        s.swapEdges()
        m.inverseUpMovement()
        m.frontMovement()
        m.frontMovement()
        m.upMovement()
    def GY():
    def YO():
        m.leftMovement()
        m.leftMovement()
        s.swapEdges()
        m.leftMovement()
        m.leftMovement()
    def OY():
    def YB():
        m.upMovement()
        m.behindMovement()
        m.behindMovement()
        m.inverseUpMovement()
        s.swapEdges()
        m.upMovement()
        m.behindMovement()
        m.behindMovement()
        m.inverseUpMovement()
    def BY():
    def WR():
    def RW():
    def WG():
    def GW():
    def WO():
        s.swapEdges()
    def OW():
    def WB():
    def BW():
