from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

for i in range(1,8):
    robotArm.moveRight()
for i in range(1,2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

for i in range(1,8):
    for i in range(1,3):
        robotArm.moveLeft()
    for i in range(1,2):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:

robotArm.wait()


