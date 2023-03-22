#The step is the particle and it is bringing - charge, deps

class Step():
	def __init__(self):
		self.time = 0
		self.x0 = 0
		self.y0 = 0
		self.z0 = 0
		self.x1 = 0
		self.y1 = 0
		self.z1 = 0
		self.ekin = 0
		self.eDep = 0
		pass
	def SetXYZ0(self, x0, y0, z0):
		self.x0 = x0
		self.y0 = y0
		self.z0 = z0
		pass
	def SetXYZ1(self, x1, y1, z1):
		self.x1 = x1
		self.y1 = y1
		self.z1 = z1
		pass
	def GetXYZ0(self):
		return [self.x0, self.y0, self.z0]
		pass
	def GetXYZ1(self):
		return [self.x1, self.y1, self.z1]
		pass
	def SetTime(self, time):
		self.time=time
		pass
	def GetTime(self):
		return self.time
		pass
	def SetEdep(self, edep):
		self.eDep=edep
		pass
	def SetEkin(self, ekin):
		self.eKin=ekin
		pass
	def GetEdep(self):
		return self.eDep
	def GetEkin(self):
		return self.eKin
		