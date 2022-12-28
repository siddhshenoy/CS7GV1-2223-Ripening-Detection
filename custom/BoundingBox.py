
class BoundingBox:
	def __init__(self):
		self.centreX = 0
		self.centreY = 0
		self.width = 0
		self.height = 0
		self.startX = 0
		self.startY = 0
		self.endX = 0
		self.endY = 0

	def set_centre(self, x, y):
		self.centreX = x
		self.centreY = y

	def set_dimensions(self, w, h):
		self.width = w
		self.height = h

	def calculate_boundaries(self):
		self.startX = int(self.centreX - (self.width // 2))
		self.startY = int(self.centreY - (self.height // 2))
		self.endX = int(self.centreX + (self.width // 2))
		self.endY = int(self.centreY + (self.height // 2))

	def get_boundaries(self):
		return self.startX, self.startY, self.endX, self.endY
