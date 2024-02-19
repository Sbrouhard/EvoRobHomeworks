import pyrosim.pyrosim as pyrosim

def main():
    Create_World()
    Create_Robot()

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name= f"Box 1", pos=[5, 5, 1] , size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name= f"Torso", pos=[1.5, 1.5, 1.5] , size=[1,1,1])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 1.5, 1])
    pyrosim.Send_Cube(name= f"BackLeg", pos=[-0.5, 0, -0.5] , size=[1,1,1])

    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 1.5, 1])
    pyrosim.Send_Cube(name= f"Frontleg", pos=[0.5, 0, -0.5] , size=[1,1,1])




    pyrosim.End()



main()