import pyrosim.pyrosim as pyrosim
import random

def main():
    Create_World()
    Create_Body()
    Create_Brain()

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name= f"Box 1", pos=[5, 5, 1] , size=[1,1,1])
    pyrosim.End()

def Create_Body():
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name= f"Torso", pos=[1.5, 1.5, 1.5] , size=[1,1,1])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 1.5, 1])
    pyrosim.Send_Cube(name= f"BackLeg", pos=[-0.5, 0, -0.5] , size=[1,1,1])

    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 1.5, 1])
    pyrosim.Send_Cube(name= f"Frontleg", pos=[0.5, 0, -0.5] , size=[1,1,1])




    pyrosim.End()

def Create_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # Generating Sensor Neurons
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLeg")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")

    # Generating Motor Neurons
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    # Connecting Neurons
    last_sensor_index = 1
    last_motor_index = 4
    for i in range(0, last_sensor_index + 1):
        for j in range(last_sensor_index + 1, last_motor_index + 1):
            pyrosim.Send_Synapse(sourceNeuronName = i, targetNeuronName = j, weight= (2 *  random.random()) - 1)




    pyrosim.End()





main()