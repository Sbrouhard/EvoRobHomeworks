import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.values = np.zeros(c.simulationSteps)
        self.jointName = jointName



    def SetValue(self, robotId, desired_angle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL,

            targetPosition =  desired_angle,
            maxForce = 300)
        
           
    
    