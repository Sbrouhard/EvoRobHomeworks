import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import numpy as np

class ROBOT:
    
    def __init__(self):
        # Creating Empty Dictionaries for sensors and motors
        self.sensors = {}
        self.motors = {}

        self.zcoords = []

        # Loading body of the robot and loading pyrosim data
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Loading sensors into self.sensors and neural network
        self.Prepare_To_Sense()
        self.nn = NEURAL_NETWORK("brain.nndf")

        # Loading Motors
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)



    # Loads values for each sensor into the index associated with timeSetp
    def Sense(self, timeStep):
        for sensor in self.sensors.values():
            sensor.Get_Value(timeStep)
    
    # Takes value in motor neuron from NN and causes respective motor to act on 
    # Motor neurons value
    def Act(self, timeStep):
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    desired_angle = self.nn.Get_Value_Of(neuronName)
                    for motor in self.motors.values():
                        if motor.Get_Joint_Name().decode('utf-8') == jointName:
                            motor.SetValue(self.robotId, desired_angle)
    def Think(self):
        self.nn.Update()
        stateOfLinkZero = p.getLinkState(self.robotId,0)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero =  stateOfLinkZero[0]
        xCoordOfLinkZero = positionOfLinkZero[0]

        fitness = xCoordOfLinkZero
        
        f = open("fitness.txt", "w")
        f.write(str(xCoordOfLinkZero))
        f.close()








