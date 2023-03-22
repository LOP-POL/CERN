#!/usr/bin/env python

class Word():
	def __init__(self, x, y):
		self.hits=[]
		self.time = 0
		self.x = 0
		self.y = 0
		pass
	def setTime(self, time):
		self.time=time
		pass
	def addHit(self, hit):
		self.hits.append(hit)
		pass
	def getHits():
		return self.hits;
	def getX():
		return self.x
	def getY():
		return self.y
	def getTime():
		return self.time
	
		