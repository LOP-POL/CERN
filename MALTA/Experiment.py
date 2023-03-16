import numpy as np
from step import Step
import math
import random

def StartOfEvent():
    return
class Event():
    def __init__(self,name,threshold,steps = 512):
        self.min = 200
        self.max = 2500
        self.name = name
        self.threshold = threshold
        self.hits = []
        self.steps = steps
        self.arrOfSteps = []
    
    #Since we want to control the numer of steps we will create
    #a certian number of steps in a range 
    #and assign them each a position
    # In the same function if a hit is gretae than the thrshold it will be added to the hits array
    def CreateSteps(self):
        for n in range(self.steps):
            n = Step() 
            # This makes sure that the ranom number generated is going to be either 0 to 256
            # 
            forP = random.randrange(10,256)
            # the array is going to be random

            #The position is going to be for coordinates x0,x1,y0,y1,z0,z1
            newP = np.ones((1,6))
            newP1 = np.floor(np.random.random((1,6)) * forP)
            newP2 = map(lambda x : math.floor(x),newP1)
            
            newP *= newP1
            n.position = newP
            # Charge is also ranomly generated and it will be compared with the threshold
            n.charge = math.floor(random.random()*500)

            self.arrOfSteps.append(n)
            print(n.position)
            print(n.charge)

            #A step is added to the hits array if its charge is greater than the threshold

        for step in self.arrOfSteps:
            if step.charge>self.threshold:
                step.hit=True
                self.hits.append(step)
                print(step.charge)

        print("Number of steps\n")
        print(len(self.arrOfSteps))
        print("The Number of hits:\n")
        print(len(self.hits))


#This is a test to see how the code will work
Exp1 = Event("alpha",400)
print(Exp1.name)
Exp1.CreateSteps()


