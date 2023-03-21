import numpy as np
import math
import random
from step import Step
from hit import Hit

class Experiment():
    def __init__(self,name):
        self.name = name
        self.hits = []

        self.pixel = np.zeros((1,65536),dtype=int).reshape(math.floor(math.sqrt(65536)),math.floor(math.sqrt(65536)))
    def StartOfEvent(self):
            s = Step() 
            # This makes sure that the random number generated is going to be either 0 to 256 
            #Need to chnage this to make it micro meters instead of pixel coordinate
            forP = random.randrange(10,math.sqrt(65536))

            # the array is going to be random

            #The position is going to be for coordinates x0,x1,y0,y1,z0,z1
            newP = np.ones((1,2))
            newP1 = np.floor(np.random.random((1,2)) * forP)

            newP *= newP1
            
            s.position = newP.astype(int)
            # Charge is also ranomly generated and it will be compared with the threshold
            s.charge = math.floor(random.random()*10000)

    def CreateHits(self,numberOfhits):
           
            for H in range(numberOfhits):
                H = Hit()
                forP = random.randrange(10,math.sqrt(65536))
                newP = np.ones((1,2))
                newP1 = np.floor(np.random.random((1,2)) * forP)

                newP *= newP1

                Hit.position = newP.astype(int) 
                H.charge = math.floor(random.random()*10000)
                H.setPix(self.pixel)
            return 
    def EndOfEvent():
        
        pass
if __name__ == "main":
     pass