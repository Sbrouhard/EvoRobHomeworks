import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for i in range(0, 1000):
    print(i)
    time.sleep(0.0066)
    p.stepSimulation()

p.disconnect()
