import Movement as m
import Swap as s

#Deplacement des coins pour pouvoir les échanger facilement : 
#le résultat de chaque fonction va se trouver en position 
#YGR pour etre échangé avec celui en position OBW
#puis on met le nouveau coin dans la position où il était
#(nom de la classe à changer)
#Coins mis plusieurs fois car dépent de leur orientation (3 orientations différentes par coin)
class DeplacementCorners:
    def WOB:
    def WBR:
        m.right()
        m.right()
        s.swapCorners()
        m.right()
        m.right()
    def WRG:
        m.front()
        m.front()
        m.inverseDown()
        s.swapCorners()
        m.down()
        m.front()
        m.front()
    def WGO:
        m.front()
        s.swapCorners()
        m.front()
    def BOY:
        m.inverseDown()
        m.inverseFront()
        s.swapCorners()
        m.front()
        m.down()
    def BYR:
        m.right()
        s.swapCorners()
        m.inverseRight()
    def BRW:
        m.right()
        m.down()
        s.swapCorners()
        m.inverseDown()
        m.inverseRight()
    def BWO:
    def RBY:
        m.down()
        m.right()
        m.down()
        s.swapCorners()
        m.inverseDown()
        m.inverseRight()
        m.inverseDown()
    def RYG
    def RGW:
        m.front()
        s.swapCorners()
        m.inverseFront()
    def RWB
    def GRY
    def GYO
    def GOW
    def GWR:
        m.inverseRight()
        s.swapCorners()
        m.right()
    def OGY:
        m.inverseFront()
        s.swapCorners()
        m.front()
    def OYB
    def OBW
    def OWG
    def YBO:
        m.down()
        m.down()
        s.swapCorners()
        m.down()
        m.down()
    def YOG:
        m.inverseDown()
        s.swapCorners()
        m.down()
    def YGR:
        s.swapCorners()
    def YRB:
        m.down()
        s.swapCorners()
        m.inverseDown()