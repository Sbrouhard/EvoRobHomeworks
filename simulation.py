from robot import ROBOT
from world import WORLD
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import numpy as np



class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    
    def Run(self):

        for timeStep in range(0, c.simulationSteps):
            time.sleep(0.001)
            p.stepSimulation()

            self.robot.Sense(timeStep)
            self.robot.Think()
            self.robot.Act(timeStep)
        
        

    def __del__(self):
        p.disconnect()


