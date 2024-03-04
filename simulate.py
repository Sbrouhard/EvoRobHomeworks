import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import random
import constants as c
from simulation import SIMULATION






# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())



# p.setGravity(0,0,-9.8)

# p.loadSDF("world.sdf")


# robotId = p.loadURDF("body.urdf")
# planeId = p.loadURDF("plane.urdf")



# pyrosim.Prepare_To_Simulate(robotId)

# x = np.linspace(0, 2 * np.pi, 1000)
# targetAngles = np.sin(x) * (np.pi / 4.0)




# FrontLegTargetAngles = np.zeros(1000)
# for i in range(0, FrontLegTargetAngles.size):
#      FrontLegTargetAngles[i] = c.FrontLegAmplitude * np.sin(c.FrontLegFrequency * x[i] + c.FrontLegPhaseOffset) 

# BackLegTargetAngles = np.zeros(1000)
# for i in range(0, BackLegTargetAngles.size):
#      BackLegTargetAngles[i] = c.BackLegAmplitude * np.sin(c.BackLegFrequency * x[i] + c.BackLegPhaseOffset)  



    
# with open('data/frontLegSinvalues.npy', 'wb') as f:
#      np.save(f, FrontLegTargetAngles)\
     
       
# with open('data/backLegSinvalues.npy', 'wb') as f:
#      np.save(f, BackLegTargetAngles)\

# # with open('data/frontTouchSensorData.npy', 'wb') as f:
# #     numpy.save(f, frontLegSensorValues)

# p.disconnect()


simulation = SIMULATION()
simulation.Run()
