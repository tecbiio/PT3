import maestro
import Movement
import MovementCube
import RubiksCube
import time

"""cube = RubiksCube.RubiksCube()
mc = MovementCube.Movement()
mc.up(cube, 5)
print(cube.getTab())"""
servo = maestro.Controller()
cube = RubiksCube.RubiksCube()
move = Movement.Movement()
move.initialisation()
print(cube.getTab())
move.x(cube)
print(cube.getTab())
move.x(cube)
print(cube.getTab())
move.x(cube)
print(cube.getTab())
move.y(cube)
print(cube.getTab())
move.y(cube)
print(cube.getTab())
move.y(cube)
print(cube.getTab())
move.right(cube)
print(cube.getTab())
move.fin()
servo.close()
