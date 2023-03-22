#!/usr/bin/env python

from hit import Hit
from word import Word

class Group():
	
	#Create a group given the pixel coordinates
	def __init__(self,col,row):
		self.words = []
		self.ncols = 2
		self.nrows = 8
		self.col = col
		self.row = row
		pass
	
	def setCol(self,col):
		self.col=col
		pass
		
	def setRow(self,row):
		self.row=row
		pass
	
	def getCol(self):
		return self.col

	def getRow(self):
		return self.row

	def getNCols(self):
		return self.ncols

	def getNRows(self):
		return self.nrows
	
	def clear(self):
		self.hits=[]
		pass
		
	# 
	#
	def processHits(self,hits):
		word = Word(self.col,self.row)
		for hit in hits:
			if hit.GetX() >= self.col and hit.GetX() < (self.col+self.ncols) and hit.GetY() >= self.row and hit.GetY() < (self.row+self.nrows):
				word = self.hits.append(hit)
				pass
			pass
		self.words.append(word)
	
	def getWords(self):
		return self.words