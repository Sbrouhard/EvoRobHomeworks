import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy





physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())



p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")


robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")



pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(200)
frontLegSensorValues = numpy.zeros(200)


for i in range(0, 200):
    time.sleep(0.001)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


with open('data/backTouchSensorData.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)\

with open('data/frontTouchSensorData.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

p.disconnect()
