from solution import SOLUTION
import constants
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(0, constants.numberOfGenerations):
            print(currentGeneration)
            self.Evolve_For_One_Generation()
        self.parent.Evaluate("GUI")
    

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()




    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        print(f'PARENT FITNESS {self.parent.fitness}  CHILD FITNESS {self.child.fitness}')
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child
            print("--------SWAPPING----------")

