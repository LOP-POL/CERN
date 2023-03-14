import numpy as np
from step import Step
import math
import random

class Experiment:
    def __init__(self,name,threshold,time,steps = math.floor(random.random()*10)):
        self.min = 200
        self.max = 2500
        self.name = name
        self.threshold = threshold
        self.hits = []
        self.steps = steps
        self.time = time
        self.arrOfSteps = []
    #Since we want to control the numer of steps we will create
    #a certian number of steps in a range 
    #and assign them each a position
    def CreateSteps(self):
        for n in range(self.steps):
            n = Step() 
            # the array is going to be random
            #The position is going to be for coordinates x0,x1,y0,y1,z0,z1
            newP = np.arange(1,7) * math.floor(random.random()*10)
            n.position = newP
            n.charge = math.floor(random.random()*500)
            self.arrOfSteps.append(n)
            print(n.position)
            print(n.charge)

    def CreateHits(self):
        for step in self.arrOfSteps:
            if step.charge>self.threshold:
                self.hits.append(step)
                print(step.charge)

        print("The Number of hits:\n")
        print(len(self.hits))



Exp1 = Experiment("alpha",400,20)

print(Exp1.name)

Exp1.CreateSteps()
print("hits\n")
Exp1.CreateHits()
