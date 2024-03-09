import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import random
import constants as c
from simulation import SIMULATION
import os



os.system("python3 generate.py")
simulation = SIMULATION()
simulation.Run()
