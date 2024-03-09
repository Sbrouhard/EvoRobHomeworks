import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    
    def __init__(self):
        self.sensors = {}
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.nn = NEURAL_NETWORK("brain.nndf")

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)



    def Sense(self, timeStep):
        for sensor in self.sensors.values():
            sensor.Get_Value(timeStep)
    
    def Act(self, timeStep):
        for motor in self.motors.values():
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    desired_angle = self.nn.Get_Value_Of(neuronName)
                    motor.SetValue(self.robotId, desired_angle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()







