#!/usr/bin/env python

from digit import Digit

class Merger():
	def __init__(self):
		self.digits=[]
		pass
	def processWords(self, words):
		for word in words:
			self.digits.append(word)
			pass
	def getDigits(self):
		return self.digits
		