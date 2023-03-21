import numpy as np
import math
import random

class Pixel():
    def __init__(self):
            
        self.delayVsCharge=[
        [0.20,70.0], #0
        [0.22,50.0], #1
        [0.25,40.0], #2
        [0.40,20.0], #3
        [0.60,14.5], #4
        [1.00,10.0], #5
        [1.50,7.50], #6
        [2.00, 6.0], #7
        [2.60, 5.5], #8
        [3.00, 5.0], #9
        ]

        #Internal propagation delay of the transistors in nanoseconds
        self.prop_delay=2

        #Threshold of the pixel in electrons
        self.threshold=230

        #Threshold noise
        self.threshold_rms=23

        #The size of the pixel
        self.pixelSize = 262144

        pass

        # the matrix is made it will be 512 by 512 because 512^2 = 262144
        self.Grid = np.zeros((1,self.pixelSize),dtype=int).reshape(math.floor(math.sqrt(self.pixelSize)),
                                                                    math.floor(math.sqrt(self.pixelSize))) 