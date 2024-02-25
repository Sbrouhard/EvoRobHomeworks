import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import random





physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())



p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")


robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")



pyrosim.Prepare_To_Simulate(robotId)

x = np.linspace(0, 2 * np.pi, 1000)
targetAngles = np.sin(x) * (np.pi / 4.0)


FrontLegAmplitude = np.pi/4
FrontLegFrequency = 5
FrontLegPhaseOffset = np.pi/4

FrontLegTargetAngles = np.zeros(1000)
for i in range(0, FrontLegTargetAngles.size):
     FrontLegTargetAngles[i] = FrontLegAmplitude * np.sin(FrontLegFrequency * x[i] + FrontLegPhaseOffset) 

BackLegAmplitude = np.pi/4
BackLegFrequency = 5
BackLegPhaseOffset = 0

BackLegTargetAngles = np.zeros(1000)
for i in range(0, BackLegTargetAngles.size):
     BackLegTargetAngles[i] = BackLegAmplitude * np.sin(BackLegFrequency * x[i] + BackLegPhaseOffset)  


for i in range(0, 1000):
    time.sleep(0.001)
    p.stepSimulation()
    pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,

    jointName = b"Torso_BackLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition =  BackLegTargetAngles[i],

    maxForce = 60)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,

    jointName = b"Torso_FrontLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = FrontLegTargetAngles[i],

    maxForce = 60)


# with open('data/backTouchSensorData.npy', 'wb') as f:
#     numpy.save(f, backLegSensorValues)\
    
with open('data/frontLegSinvalues.npy', 'wb') as f:
     np.save(f, FrontLegTargetAngles)\
     
       
with open('data/backLegSinvalues.npy', 'wb') as f:
     np.save(f, BackLegTargetAngles)\

# with open('data/frontTouchSensorData.npy', 'wb') as f:
#     numpy.save(f, frontLegSensorValues)

p.disconnect()
