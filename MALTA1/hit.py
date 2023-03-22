#!/usr/bin/env python

#definition of a Hit

class Hit():
	def __init__(self, x=0, y=0, time=0):
		self.x=x
		self.y=y
		self.time=time
		pass
	def SetX(self,x):
		self.x=x
		pass
	def SetX(self,y):
		self.y=y
		pass
	def SetTime(self,time):
		self.time=time
		pass
	def GetX(self):
		return self.x
	def GetY(self):
		return self.y
	def SetTime(self):
		return self.time
	pass
