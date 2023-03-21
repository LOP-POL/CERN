import numpy as np
import random
import math
from step import Step

class Process():
    def __init__(self,pixels = 65536):
        self.pixels = pixels
    def MakeStep(self):
        n = Step() 
        # This makes sure that the ranom number generated is going to be either 0 to 256 
        forP = random.randrange(10,math.sqrt(self.pixels))
        # the array is going to be random

        #The position is going to be for coordinates x0,y0
        newP = np.ones((1,2))
        newP1 = np.floor(np.random.random((1,2)) * forP)

        newP *= newP1
        
        n.position = newP.astype(int)
        # Charge is also ranomly generated and it will be compared with the threshold
        n.charge = math.floor(random.random()*10000)
        return n
step = Process().MakeStep()
stepCharge = step.charge
stepPosition = step.position

print(stepPosition)
print(stepCharge)
