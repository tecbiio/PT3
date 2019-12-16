# -*- coding: utf-8 -*-
import RubiksCube
import maestro
import MovementRobot
import MovementCube
import time

""" Les fonctions de mouvements dans ce fichier permettent d'appeler directement
les fonctions concernées pour le cube virtuel et le cube physique.
Les fonctions prennent en param le cube courant en premier param et l'id
correspondant à la couleur de la face, en face de la caméra.
(Récupérable via le cube virtuel)
Savoir la couleur de la face en face et de la face au dessus nous
permet de savoir dans quelle disposition se trouve le cube et donc comment
tourner virtuellement le cube sans poser de
problèmes au niveau des coordonnées pour les facettes
Les mouvements suivent juste leur code puisque c'est au cube virtuel de
s'adapter """

class Movement():

    def initialisation(self):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mr.initialisation(servo)
        servo.close()

    def fin(self):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mr.fin(servo)
        servo.close()

    def right(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        print("id:",id,"topid:",topid)
        if (id == 0):
            if (topid == 1):
                mc.down(cube, id)
            elif (topid == 3):
                mc.up(cube, id)
            elif (topid == 4):
                mc.right(cube, id)
            elif (topid == 5):
                mc.left(cube,id)
        elif (id == 1):
            if (topid == 0):
                mc.up(cube, id)
            elif (topid == 2):
                mc.down(cube, id)
            elif (topid == 4):
                mc.right(cube, id)
            elif (topid == 5):
                mc.left(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.up(cube, id)
            elif (topid == 3):
                mc.down(cube, id)
            elif (topid == 4):
                mc.right(cube, id)
            elif (topid == 5):
                mc.left(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.down(cube, id)
            elif (topid == 2):
                mc.up(cube, id)
            elif (topid == 4):
                mc.right(cube, id)
            elif (topid == 5):
                mc.left(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.right(cube, id)
            elif (topid == 1):
                mc.up(cube, id)
            elif (topid == 2):
                mc.left(cube, id)
            elif (topid == 3):
                mc.down(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.right(cube, id)
            elif (topid == 1):
                mc.down(cube, id)
            elif (topid == 2):
                mc.left(cube, id)
            elif (topid == 3):
                mc.up(cube, id)
        mr.right(servo)
        servo.close()

    def invRight(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.invDown(cube, id)
            elif (topid == 3):
                mc.invUp(cube, id)
            elif (topid == 4):
                mc.invRight(cube, id)
            elif (topid == 5):
                mc.invLeft(cube, id)
        elif (id == 1):
            if (topid == 0):
                mc.invUp(cube, id)
            elif (topid == 2):
                mc.invDown(cube, id)
            elif (topid == 4):
                mc.invRight(cube, id)
            elif (topid == 5):
                mc.invLeft(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.invUp(cube, id)
            elif (topid == 3):
                mc.invDown(cube, id)
            elif (topid == 4):
                mc.invRight(cube, id)
            elif (topid == 5):
                mc.invLeft(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.invDown(cube, id)
            elif (topid == 2):
                mc.invUp(cube, id)
            elif (topid == 4):
                mc.invRight(cube, id)
            elif (topid == 5):
                mc.invLeft(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.invRight(cube, id)
            elif (topid == 1):
                mc.invUp(cube, id)
            elif (topid == 2):
                mc.invLeft(cube, id)
            elif (topid == 3):
                mc.invDown(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.invRight(cube, id)
            elif (topid == 1):
                mc.invDown(cube, id)
            elif (topid == 2):
                mc.invLeft(cube, id)
            elif (topid == 3):
                mc.invUp(cube, id)
        mr.invRight(servo)
        servo.close()

    def left(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.up(cube, id)
            elif (topid == 3):
                mc.down(cube, id)
            elif (topid == 4):
                mc.left(cube, id)
            elif (topid == 5):
                mc.right(cube,id)
        elif (id == 1):
            if (topid == 0):
                mc.down(cube, id)
            elif (topid == 2):
                mc.up(cube, id)
            elif (topid == 4):
                mc.left(cube, id)
            elif (topid == 5):
                mc.right(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.down(cube, id)
            elif (topid == 3):
                mc.up(cube, id)
            elif (topid == 4):
                mc.left(cube, id)
            elif (topid == 5):
                mc.right(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.up(cube, id)
            elif (topid == 2):
                mc.down(cube, id)
            elif (topid == 4):
                mc.left(cube, id)
            elif (topid == 5):
                mc.right(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.left(cube, id)
            elif (topid == 1):
                mc.down(cube, id)
            elif (topid == 2):
                mc.right(cube, id)
            elif (topid == 3):
                mc.up(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.left(cube, id)
            elif (topid == 1):
                mc.up(cube, id)
            elif (topid == 2):
                mc.right(cube, id)
            elif (topid == 3):
                mc.down(cube, id)
        mr.left(servo)
        servo.close()

    def invLeft(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.invUp(cube, id)
            elif (topid == 3):
                mc.invDown(cube, id)
            elif (topid == 4):
                mc.invLeft(cube, id)
            elif (topid == 5):
                mc.invRight(cube, id)
        elif (id == 1):
            if (topid == 0):
                mc.invDown(cube, id)
            elif (topid == 2):
                mc.invUp(cube, id)
            elif (topid == 4):
                mc.invLeft(cube, id)
            elif (topid == 5):
                mc.invRight(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.invDown(cube, id)
            elif (topid == 3):
                mc.invUp(cube, id)
            elif (topid == 4):
                mc.invLeft(cube, id)
            elif (topid == 5):
                mc.invRight(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.invUp(cube, id)
            elif (topid == 2):
                mc.invDown(cube, id)
            elif (topid == 4):
                mc.invLeft(cube, id)
            elif (topid == 5):
                mc.invRight(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.invLeft(cube, id)
            elif (topid == 1):
                mc.invDown(cube, id)
            elif (topid == 2):
                mc.invRight(cube, id)
            elif (topid == 3):
                mc.invUp(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.invLeft(cube, id)
            elif (topid == 1):
                mc.invUp(cube, id)
            elif (topid == 2):
                mc.invRight(cube, id)
            elif (topid == 3):
                mc.invDown(cube, id)
        mr.invLeft(servo)
        servo.close()

    def up(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.right(cube, id)
            elif (topid == 3):
                mc.left(cube, id)
            elif (topid == 4):
                mc.up(cube, id)
            elif (topid == 5):
                mc.down(cube,id)
        elif (id == 1):
            if (topid == 0):
                mc.left(cube, id)
            elif (topid == 2):
                mc.right(cube, id)
            elif (topid == 4):
                mc.up(cube, id)
            elif (topid == 5):
                mc.down(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.left(cube, id)
            elif (topid == 3):
                mc.right(cube, id)
            elif (topid == 4):
                mc.up(cube, id)
            elif (topid == 5):
                mc.down(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.right(cube, id)
            elif (topid == 2):
                mc.left(cube, id)
            elif (topid == 4):
                mc.up(cube, id)
            elif (topid == 5):
                mc.down(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.up(cube, id)
            elif (topid == 1):
                mc.left(cube, id)
            elif (topid == 2):
                mc.down(cube, id)
            elif (topid == 3):
                mc.right(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.up(cube, id)
            elif (topid == 1):
                mc.right(cube, id)
            elif (topid == 2):
                mc.down(cube, id)
            elif (topid == 3):
                mc.left(cube, id)
        mr.up(servo)
        servo.close()

    def invUp(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.invRight(cube, id)
            elif (topid == 3):
                mc.invLeft(cube, id)
            elif (topid == 4):
                mc.invUp(cube, id)
            elif (topid == 5):
                mc.invDown(cube, id)
        elif (id == 1):
            if (topid == 0):
                mc.invLeft(cube, id)
            elif (topid == 2):
                mc.invRight(cube, id)
            elif (topid == 4):
                mc.invUp(cube, id)
            elif (topid == 5):
                mc.invDown(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.invLeft(cube, id)
            elif (topid == 3):
                mc.invRight(cube, id)
            elif (topid == 4):
                mc.invUp(cube, id)
            elif (topid == 5):
                mc.invDown(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.invRight(cube, id)
            elif (topid == 2):
                mc.invLeft(cube, id)
            elif (topid == 4):
                mc.invUp(cube, id)
            elif (topid == 5):
                mc.invDown(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.invUp(cube, id)
            elif (topid == 1):
                mc.invLeft(cube, id)
            elif (topid == 2):
                mc.invDown(cube, id)
            elif (topid == 3):
                mc.invRight(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.invUp(cube, id)
            elif (topid == 1):
                mc.invRight(cube, id)
            elif (topid == 2):
                mc.invDown(cube, id)
            elif (topid == 3):
                mc.invLeft(cube, id)
        mr.invUp(servo)
        servo.close()

    def down(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.left(cube, id)
            elif (topid == 3):
                mc.right(cube, id)
            elif (topid == 4):
                mc.down(cube, id)
            elif (topid == 5):
                mc.up(cube,id)
        elif (id == 1):
            if (topid == 0):
                mc.right(cube, id)
            elif (topid == 2):
                mc.left(cube, id)
            elif (topid == 4):
                mc.down(cube, id)
            elif (topid == 5):
                mc.up(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.right(cube, id)
            elif (topid == 3):
                mc.left(cube, id)
            elif (topid == 4):
                mc.down(cube, id)
            elif (topid == 5):
                mc.up(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.left(cube, id)
            elif (topid == 2):
                mc.right(cube, id)
            elif (topid == 4):
                mc.down(cube, id)
            elif (topid == 5):
                mc.up(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.down(cube, id)
            elif (topid == 1):
                mc.right(cube, id)
            elif (topid == 2):
                mc.up(cube, id)
            elif (topid == 3):
                mc.left(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.down(cube, id)
            elif (topid == 1):
                mc.left(cube, id)
            elif (topid == 2):
                mc.up(cube, id)
            elif (topid == 3):
                mc.right(cube, id)
        mr.down(servo)
        servo.close()

    def invDown(self, cube):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mc = MovementCube.Movement()
        id = cube.getValTab(0, 1, 1) #Couleur de la face en face
        topid = cube.getValTab(4, 1, 1) #Couleur de la face au dessus
        if (id == 0):
            if (topid == 1):
                mc.invLeft(cube, id)
            elif (topid == 3):
                mc.invRight(cube, id)
            elif (topid == 4):
                mc.invDown(cube, id)
            elif (topid == 5):
                mc.invUp(cube, id)
        elif (id == 1):
            if (topid == 0):
                mc.invRight(cube, id)
            elif (topid == 2):
                mc.invLeft(cube, id)
            elif (topid == 4):
                mc.invDown(cube, id)
            elif (topid == 5):
                mc.invUp(cube, id)
        elif (id == 2):
            if (topid == 1):
                mc.invRight(cube, id)
            elif (topid == 3):
                mc.invLeft(cube, id)
            elif (topid == 4):
                mc.invDown(cube, id)
            elif (topid == 5):
                mc.invUp(cube, id)
        elif (id == 3):
            if (topid == 0):
                mc.invLeft(cube, id)
            elif (topid == 2):
                mc.invRight(cube, id)
            elif (topid == 4):
                mc.invDown(cube, id)
            elif (topid == 5):
                mc.invUp(cube, id)
        elif (id == 4):
            if (topid == 0):
                mc.invDown(cube, id)
            elif (topid == 1):
                mc.invRight(cube, id)
            elif (topid == 2):
                mc.invUp(cube, id)
            elif (topid == 3):
                mc.invLeft(cube, id)
        elif (id == 5):
            if (topid == 0):
                mc.invDown(cube, id)
            elif (topid == 1):
                mc.invLeft(cube, id)
            elif (topid == 2):
                mc.invUp(cube, id)
            elif (topid == 3):
                mc.invRight(cube, id)
        mr.invDown(servo)
        servo.close()

    def pictures(self):
        servo = maestro.Controller()
        mr = MovementRobot.Movement()
        mr.x(servo)
        time.sleep(5) #Temps de prise de photo
        mr.x(servo)
        time.sleep(5) #Temps de prise de photo
        mr.x(servo)
        time.sleep(5) #Temps de prise de photo
        mr.y(servo)
        time.sleep(5) #Temps de prise de photo
        mr.y(servo)
        time.sleep(5) #Temps de prise de photo
        mr.y(servo)
        time.sleep(5) #Temps de prise de photo
        mr.y(servo)
        mr.x(servo)
        servo.close()
