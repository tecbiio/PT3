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
        m.rightMovement()
        m.rightMovement()
        s.swapCorners()
        m.rightMovement()
        m.rightMovement()
    def WRG:
        m.frontMovement()
        m.frontMovement()
        m.inverseDownMovement()
        s.swapCorners()
        m.downMovement()
        m.frontMovement()
        m.frontMovement()
    def WGO:
        m.frontMovement()
        s.swapCorners()
        m.frontMovement()
    def BOY:
        m.inverseDownMovement()
        m.inverseFrontMovement()
        s.swapCorners()
        m.frontMovement()
        m.downMovement()
    def BYR:
        m.rightMovement()
        s.swapCorners()
        m.inverseRightMovement()
    def BRW:
        m.rightMovement()
        m.downMovement()
        s.swapCorners()
        m.inverseDownMovement()
        m.inverseRightMovement()
    def BWO:
    def RBY:
        m.downMovement()
        m.rightMovement()
        m.downMovement()
        s.swapCorners()
        m.inverseDownMovement()
        m.inverseRightMovement()
        m.inverseDownMovement()
    def RYG
    def RGW:
        m.frontMovement()
        s.swapCorners()
        m.inverseFrontMovement()
    def RWB
    def GRY
    def GYO
    def GOW
    def GWR:
        m.inverseRightMovement()
        s.swapCorners()
        m.rightMovement()
    def OGY:
        m.inverseFrontMovement()
        s.swapCorners()
        m.frontMovement()
    def OYB
    def OBW
    def OWG
    def YBO:
        m.downMovement()
        m.downMovement()
        s.swapCorners()
        m.downMovement()
        m.downMovement()
    def YOG:
        m.inverseDownMovement()
        s.swapCorners()
        m.downMovement()
    def YGR:
        s.swapCorners()
    def YRB:
        m.downMovement()
        s.swapCorners()
        m.inverseDownMovement()