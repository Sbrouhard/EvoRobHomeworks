import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

for i in range(0, 1000):
    print(i)
    time.sleep(0.0066)
    p.stepSimulation()

p.disconnect()
