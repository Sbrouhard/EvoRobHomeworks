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



for i in range(0, 100000):
    time.sleep(0.001)
    p.stepSimulation()
    pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,

    jointName = b"Torso_BackLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = 3.1415926 / 4.0,

    maxForce = 500)


# with open('data/backTouchSensorData.npy', 'wb') as f:
#     numpy.save(f, backLegSensorValues)\

# with open('data/frontTouchSensorData.npy', 'wb') as f:
#     numpy.save(f, frontLegSensorValues)

p.disconnect()
