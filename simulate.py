import pybullet as p
import pyrosim.pyrosim as pyrosim
import time



physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")


for i in range(0, 100000):
    time.sleep(0.0066)
    p.stepSimulation()

p.disconnect()
