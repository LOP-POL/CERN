import numpy as np
import math
import random
from step import Step
from hit import Hit
from pixel import Pixel
from group import Group
from merger import Merger

class Experiment():
	def __init__(self,name="ATLAS"):
		self.name = name
		self.steps = []
		self.hits = []
		self.words = []
		self.digits = []
		self.pixel = Pixel()
		self.groups = []
		self.merger = Merger()
		self.nrows = 32
		self.ncols = 16
		self.x0 = 0
		self.x1 = 36400*self.ncols #nm
		self.y0 = 0
		self.y1 = 36400*self.nrows #nm
		self.th = 230
		self.ns = 23
		row=0
		col=0
		while col<self.ncols:
			print("create group at col=%i row=%i"%(col,row))
			group=Group(col,row)
			self.groups.append(group)
			row+=group.getNRows()
			if row>self.nrows:
				row=0
				col+=group.getNCols()
				pass
		pass
	
	def generateSteps(self, nsteps=1):
		for i in range(nsteps):
			s=Step()
			s.SetXYZ0(random.randint(self.x0,self.x1),random.randint(self.y0,self.y1),0)
			s.SetEdep(random.randint(self.th-self.ns, self.th+self.ns))
			self.steps.append(s)
			pass
		pass
		
	def getNumberOfSteps(self):
		return len(self.steps)

	def getNumberOfHits(self):
		return len(self.hits)
	
	def getNumberOfDigits(self):
		return len(self.digits)
		
	def startOfEvent(self):
		for step in self.steps:
			hit=self.pixel.processStep(step)
			if hit: self.hits.append(hit)
			pass
		pass
		
	def endOfEvent(self):
		for group in self.groups:
			group.processHits(self.hits)
			for word in group.getWords():
				self.words.append(word)
				pass
			pass
		self.merger.processWords(self.words)
		self.digits=self.merger.getDigits()
		pass
	
	def clear(self):
		self.steps = []
		self.hits = []
		self.words = []
		self.digits = []
		pass
	
	pass

if __name__ == "__main__":
	print("Experiment")
	experiment = Experiment("firstTry")
	for i in range(10):
		print("Event number:     %i" % (i+1))
		experiment.generateSteps(10)
		experiment.startOfEvent()
		print("Number of hits:   %i" % experiment.getNumberOfHits())
		experiment.endOfEvent()
		print("Number of digits: %i" % experiment.getNumberOfDigits())
		experiment.clear()
		pass