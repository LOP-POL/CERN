#!/usr/bin/env python
import random
from hit import Hit

###################################################
# Model of the MALTA Analog Pixel
# This calculates the time to threshold 
# given a charge for a given threshold
#
# @Author Carlos.Solans@cern.ch
# @Date March 2021
####################################################
class Pixel():
	
	def __init__(self):
            
		#Look up table of the amount of table needed
		#to reach to a threshold of 230 electrons
		#extracted from Ivan's thesis
		#Each element is a point (x,y)
		#x is in kiloelectrons
		#y is in nanoseconds
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

		pass

	def processStep(self,step):
		thr=random.gauss(self.threshold,self.threshold_rms)
		charge=step.GetEdep()*1 # calibrate to electrons
		if charge<thr: return None
		ttt=self.interpolate_lut(self.delayVsCharge,charge/1000.)
		hit=Hit(ttt+self.prop_delay)
		return hit
	
	def interpolate_lut(self,ref,x):
		i1=0
		v1=10000
		i2=len(ref)-1
		v2=10000
		i=0
		for point in ref:
			if point[0]<=x and x-point[0]<v1:
				i1=i
				v1=x-point[0]
				pass
			if point[0]>=x and point[0]-x<v2:
				i2=i
				v2=point[0]-x
				pass
			i+=1
			pass
		x1=ref[i1][0]
		x2=ref[i2][0]
		y1=ref[i1][1]
		y2=ref[i2][1]
		#print("i1: %i, i2: %i, x1: %.2f, x2: %.2f, y1: %.2f, y2: %.2f" % (i1,i2,x1,x2,y1,y2))
		if i2==i1: y=y2
		else: y=y1+(x-x1)*(y2-y1)/(x2-x1)
		return y
	
	pass
      