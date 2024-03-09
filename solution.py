import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random



class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)
        self.weights = (2 * self.weights) - 1

    def Evaluate(self, viewMode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system(f"python3 simulate.py {viewMode}")

        f = open("fitness.txt", "r")
        self.fitness = str(f.read())
        f.close()

        print(self.fitness)


    def Mutate(self):
        row_to_change = random.randint(0, 2)
        column_to_change = random.randint(0, 1)
        self.weights[row_to_change][column_to_change] =  random.random() * 2 - 1



    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name= f"Box 1", pos=[5, 5, 1] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name= f"Torso", pos=[1.5, 1.5, 1.5] , size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 1.5, 1])
        pyrosim.Send_Cube(name= f"BackLeg", pos=[-0.5, 0, -0.5] , size=[1,1,1])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 1.5, 1])
        pyrosim.Send_Cube(name= f"Frontleg", pos=[0.5, 0, -0.5] , size=[1,1,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # Generating Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeg")

        # Generating Motor Neurons
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        # Connecting Neurons

        for current_row in range(0, 3):
            for current_column in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName = current_row, targetNeuronName = current_column + 3, weight= self.weights[current_row][current_column])


        pyrosim.End()
