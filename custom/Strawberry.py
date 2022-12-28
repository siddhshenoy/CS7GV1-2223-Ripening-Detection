import cv2

from custom.BoundingBox import *

class Strawberry:
	def __init__(self):
		self.strawberry_class = None
		self.strawberry_image = None
		self.bounding_box = None
		self.class_colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]

	def create_bounding_box(self, bb_string, img_shape):
		#print(f"Image dimensions: {img_shape}")
		splits = bb_string.split(" ")
		for i, s in enumerate(splits):
			splits[i] = float(splits[i])
		self.strawberry_class = splits[0]
		splits[1] = splits[1] * img_shape[1]  # Calculate CentreX relative to image
		splits[2] = splits[2] * img_shape[0]  # Calculate CentreY relative to image
		splits[3] = splits[3] * img_shape[1]  # Calculate Width relative to image
		splits[4] = splits[4] * img_shape[0]  # Calculate Height relative to image
		#print(splits)
		self.bounding_box = BoundingBox()
		self.bounding_box.set_centre(splits[1], splits[2])
		self.bounding_box.set_dimensions(splits[3], splits[4])
		self.bounding_box.calculate_boundaries()

	def get_bounding_box(self):
		return self.bounding_box

	#Remove this method , unnecessary
	def set_class(self, sclass):
		self.strawberry_class = sclass

	def get_strawberry_image(self, parent_image):
		sx, sy, ex, ey = self.bounding_box.get_boundaries()
		self.strawberry_image = parent_image[sy:ey, sx:ex]

	def get_class_color(self):
		print(self.strawberry_class)
		return self.class_colors[int(self.strawberry_class)]

	def show_strawberry(self):
		cv2.imshow("Strawberry", self.strawberry_image)
		cv2.waitKey(0)