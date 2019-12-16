import maestro
import MovementRobot
import MovementCube
import Movement
import RubiksCube
import time

"""servo = maestro.Controller()
cube = RubiksCube.RubiksCube()
mr = MovementRobot.Movement()
mc = MovementCube.Movement()
mr.initialisation(servo)
mc.right(cube, 5)
mr.right(servo)
print(cube.getTab())
servo.close()"""

servo = maestro.Controller()
cube = RubiksCube.RubiksCube()
move = Movement.Movement()
mr = MovementRobot.Movement()
mr.initialisation(servo)
for i in range(0,6):
    
    print(cube.getTab())
    move.down(cube)
    move.up(cube)
    move.right(cube)
    move.left(cube)
    print(cube.getTab())
mr.fin(servo)
servo.close()
