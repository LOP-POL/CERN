import numpy as np
import math
import random
from step import Step
from hit import Hit
from pixel import Pixel

class Experiment():
    def __init__(self,name="ATLAS"):
        self.name = name
        self.hits = []
        self.pixel = Pixel()
    def StartEvent(self):
            s = Step() 
            # This makes sure that the random number generated is going to be either 0 to 256 
            #Need to chnage this to make it micro meters instead of pixel coordinate
            forP = random.randrange(10,math.sqrt(self.pixel.pixelSize))

            # the array is going to be random

            #The position is going to be for coordinates x0,x1,y0,y1,z0,z1
            newP = np.ones((1,2))
            newP1 = np.floor(np.random.random((1,2)) * forP)

            newP *= newP1
            
            s.position = newP.astype(int)
            # Charge is also ranomly generated and it will be compared with the threshold
            s.charge = math.floor(random.random()*10000)
            print("EventStartOkay")
            print(s.charge)

    def CreateHits(self,numberOfhits=10000):
           
            for H in range(numberOfhits):
                H = Hit()
                forP = random.randrange(10,math.sqrt(self.pixel.pixelSize))
                newP = np.ones((1,2))
                newP1 = np.floor(np.random.random((1,2)) * forP)

                newP *= newP1

                H.pixel = newP.astype(int) 
                self.hits.append(H)
            for each in self.hits:
                self.pixel.Grid[tuple(each.pixel[0])]=1
            print("Hits Okay")
            print(len(self.hits))
             
    def EndOfEvent(self):
        # Sorts the chip into groups
        arr = self.pixel.Grid.ravel()
        groupsColRow = []
        group = np.hsplit(arr,self.pixel.pixelSize/16)
        for i in group:
            n = np.array(i).reshape(8,2)
            groupsColRow.append(n)
        group = groupsColRow
        print("Groups okay")
        print(group[0])
        return group[0]
        
    pass
if __name__ == "main":
     pass