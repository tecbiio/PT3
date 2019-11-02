# -*- coding: utf-8 -*-
from RubiksCube import RubiksCube
from Movement import Movement

res = "Mouvement : "
end = 0
nb = int(input("Combien de fonctions de mouvements souhaitez-vous combiner ?"))
i = 0
move = Movement()
cube = RubiksCube()
while (end == 0):
    i = i + 1
    print("Quelle fonctions souhaitez-vous ajouter ?")
    print("right : 0, inverseRight : 1")
    print("left : 2, inverseLeft : 3")
    print("up : 4, inverseUp : 5")
    print("down : 6, inverseDown : 7")
    print("front : 8, inverseFront : 9")
    print("behind : 10, inverseBehind : 11")
    fct = int(input(" "))
    print("Sur quelle face voulez-vous appliquer cette fonction ?")
    print("Vert : 0")
    print("Rouge : 1")
    print("Bleu : 2")
    print("Orange : 3")
    print("Blanc : 4")
    print("Jaune : 5")
    id = int(input(" "))
    if (fct == 0):
        move.right(cube, id)
        res = res + "right" + str(id) + ", "
    if (fct == 1):
        move.inverseRight(cube, id)
        res = res + "inverseRight" + str(id) + ", "
    if (fct == 2):
        move.left(cube, id)
        res = res + "left" + str(id) + ", "
    if (fct == 3):
        move.inverseLeft(cube, id)
        res = res + "inverseLeft" + str(id) + ", "
    if (fct == 4):
        move.up(cube, id)
        res = res + "up" + str(id) + ", "
    if (fct == 5):
        move.inverseUp(cube, id)
        res = res + "inverseUp" + str(id) + ", "
    if (fct == 6):
        move.down(cube, id)
        res = res + "down" + str(id) + ", "
    if (fct == 7):
        move.inverseDown(cube, id)
        res = res + "inverseDown" + str(id) + ", "
    if (fct == 8):
        move.front(cube, id)
        res = res + "front" + str(id) + ", "
    if (fct == 9):
        move.inverseFront(cube, id)
        res = res + "inverseFront" + str(id) + ", "
    if (fct == 10):
        move.behind(cube, id)
        res = res + "behind" + str(id) + ", "
    if (fct == 11):
        move.inverseBehind(cube, id)
        res = res + "inverseBehind" + str(id) + ", "
    if (i == nb):
        end = 1
        print(cube.get_tab())
        print(res)
