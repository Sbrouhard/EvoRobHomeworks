import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.simulationSteps)

    def Get_Value(self, timeStep):
        try:
            value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            if value == -1:
                value = 0
            
            print(value)
            
            self.values[timeStep] = value
        except:
            pass
        if timeStep == c.simulationSteps - 1:
            print(self.values)
    