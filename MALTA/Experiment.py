import numpy as np
from step import Step
import math
import random

class Event():
    def __init__(self,name,threshold,steps = 512):
        self.min = 200
        self.max = 2500
        self.name = name
        self.threshold = threshold
        self.hits = []
        self.steps = steps
        self.arrOfSteps = []
        self.pixel = np.reshape(np.zeros((1,262144),dtype=int),(math.floor(math.sqrt(262144)),math.floor(math.sqrt(262144))))
    
    #Since we want to control the number of steps we will create
    #a certian number of steps in a range 
    #and assign them each a position
    # In the same function if a hit is gretae than the thrshold it will be added to the hits array
    def CreateSteps(self):
        for n in range(self.steps):
            n = Step() 
            # This makes sure that the ranom number generated is going to be either 0 to 256 
            forP = random.randrange(10,math.sqrt(262144))
            # the array is going to be random

            #The position is going to be for coordinates x0,x1,y0,y1,z0,z1
            newP = np.ones((1,2))
            newP1 = np.floor(np.random.random((1,2)) * forP)

            newP *= newP1
            
            n.position = newP.astype(int)
            # Charge is also ranomly generated and it will be compared with the threshold
            n.charge = math.floor(random.random()*500)

            self.arrOfSteps.append(n)

            #A step is added to the hits array if its charge is greater than the threshold

        for step in self.arrOfSteps:
            if step.charge>self.threshold:
                step.hit=True
                self.hits.append(step)
                # print(step.charge)
        print("Number of hits")
        print(len(self.hits))
        
    def CreateGroups(self):
        for each in self.hits:
            self.pixel[tuple(each.position[0])]=1
        return self.pixel
    
    def splitting(self):
        arr = self.pixel.ravel()
        groupsColRow = []
        group = np.hsplit(arr,self.pixel.size/16)
        for i in group:
            n = np.array(i).reshape(8,2)
            groupsColRow.append(n)
        group = groupsColRow
        print(group[0])
        return group[0]
if __name__ == "__main__":

    #This is a test to see how the code will work
    Exp1 = Event("alpha",400)
    print(Exp1.name)
    Exp1.CreateSteps()


