import maestro
import time

servo = maestro.Controller()

servo.setTarget(1, 5750)
time.sleep(1)
servo.setTarget(3, 5750)
time.sleep(1)
servo.setTarget(5, 5750)
time.sleep(1)
servo.setTarget(7, 6250)
time.sleep(1)
servo.setTarget(0, 1000) #1000 enclenchement
servo.setTarget(2, 1000)
servo.setTarget(4, 1000)
servo.setTarget(6, 1000)
time.sleep(1)

def y():
	servo.setTarget(0, 10000)
	servo.setTarget(4, 10000)
	time.sleep(1)
	servo.setTarget(3, 10000)
	servo.setTarget(7, 1000)
	time.sleep(1)
	servo.setTarget(0, 1000)
	servo.setTarget(4, 1000)
	time.sleep(1)
	servo.setTarget(2, 10000)
	servo.setTarget(6, 10000)
	time.sleep(1)
	servo.setTarget(3, 5750)
	servo.setTarget(7, 6250)
	time.sleep(1)
	servo.setTarget(2, 1000)
	servo.setTarget(6, 1000)
	time.sleep(1)	

def x():
	servo.setTarget(2, 10000)
	servo.setTarget(6, 10000)
	time.sleep(1)
	servo.setTarget(1, 10000)
	servo.setTarget(5, 1000)
	time.sleep(1)
	servo.setTarget(2, 1000)
	servo.setTarget(6, 1000)
	time.sleep(1)
	servo.setTarget(0, 10000)
	servo.setTarget(4, 10000)
	time.sleep(1)
	servo.setTarget(1, 5750)
	servo.setTarget(5, 5750)
	time.sleep(1)
	servo.setTarget(0, 1000)
	servo.setTarget(4, 1000)
	time.sleep(1)
	
def right():
	servo.setTarget(7, 10000)
	time.sleep(1)
	servo.setTarget(6, 10000)
	time.sleep(1)
	servo.setTarget(7, 6250)
	time.sleep(1)
	servo.setTarget(6, 1000)
	time.sleep(1)

def invRight():
	servo.setTarget(7, 1000)
	time.sleep(1)
	servo.setTarget(6, 10000)
	time.sleep(1)
	servo.setTarget(7, 6250)
	time.sleep(1)
	servo.setTarget(6, 1000)
	time.sleep(1)

def left():
	servo.setTarget(3, 10000)
	time.sleep(1)
	servo.setTarget(2, 10000)
	time.sleep(1)
	servo.setTarget(3, 5750)
	time.sleep(1)
	servo.setTarget(2, 1000)
	time.sleep(1)

def invLeft():
	servo.setTarget(3, 1000)
	time.sleep(1)
	servo.setTarget(2, 10000)
	time.sleep(1)
	servo.setTarget(3, 5750)
	time.sleep(1)
	servo.setTarget(2, 1000)
	time.sleep(1)

def up():
	servo.setTarget(1, 10000)
	time.sleep(1)
	servo.setTarget(0, 10000)
	time.sleep(1)
	servo.setTarget(1, 5750)
	time.sleep(1)
	servo.setTarget(0, 1000)
	time.sleep(1)

def invUp():
	servo.setTarget(1, 1000)
	time.sleep(1)
	servo.setTarget(0, 10000)
	time.sleep(1)
	servo.setTarget(1, 5750)
	time.sleep(1)
	servo.setTarget(0, 1000)
	time.sleep(1)

def down():
	servo.setTarget(5, 10000)
	time.sleep(1)
	servo.setTarget(4, 10000)
	time.sleep(1)
	servo.setTarget(5, 5750)
	time.sleep(1)
	servo.setTarget(4, 1000)
	time.sleep(1)

def invDown():
	servo.setTarget(5, 1000)
	time.sleep(1)
	servo.setTarget(4, 10000)
	time.sleep(1)
	servo.setTarget(5, 5750)
	time.sleep(1)
	servo.setTarget(4, 1000)
	time.sleep(1)
#initialisation avec photos scénario
x()
x()
x()
y()
y()
y()
#traitement
#fin
servo.setTarget(0, 10000) #1000 enclenchement
servo.setTarget(2, 10000)
servo.setTarget(4, 10000)
servo.setTarget(6, 10000)

servo.close()