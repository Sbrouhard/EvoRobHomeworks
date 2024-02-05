import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")


total = 5
for h in range(0, total):
    for j in range(0,total): 
        length = 1
        width = 1
        height = 1
        x = h
        y = 0.5
        z = j

        xzy_matrix = [x,z,y]
        lengths = [length, width, height]
        size = 0.9
        for i in range(0, 10):
            pyrosim.Send_Cube(name= f"Box {i}", pos=[xzy_matrix[0],xzy_matrix[1],xzy_matrix[2] + 1] , size=[size * lengths[0], size * lengths[1],size * lengths[2]])
            xzy_matrix = [xzy_matrix[0],xzy_matrix[1], xzy_matrix[2] + 1]
            lengths = [lengths[0] * 0.9, lengths[1] * 0.9, lengths[2] * 0.9]


pyrosim.End()


