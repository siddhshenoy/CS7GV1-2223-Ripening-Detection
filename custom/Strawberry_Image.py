""" Importing third party libraries"""
import cv2
import numpy as np

"""Importing the libraries made by us"""
from custom.GlobalVariables import *
from custom.Strawberry import *

class StrawberryImage:
	def __init__(self):
		self.instseg_file_path = None
		self.boundbox_file_path = None
		self.strawberries = []
		self.file_name_prefix = ""
		self.image_file_path = ""
		"""
			We will store all the processed image data (including original image) in this array
		"""
		self.image_data = []

	"""
		file_name_prefix: This is a numeric parameter, we will determine the text, image and instance file using this
							parameter
	"""

	def read_file(self, file_name_prefix):
		self.file_name_prefix = file_name_prefix
		self.image_file_path = GlobalVars["IM_FOLDER_PATH"] + f"/{self.file_name_prefix}.png"
		self.boundbox_file_path = GlobalVars["BB_FOLDER_PATH"] + f"/{self.file_name_prefix}.txt"
		self.instseg_file_path = GlobalVars["IS_FOLDER_PATH"] + f"/{self.file_name_prefix}.png"
		print(self.image_file_path)
		print(self.boundbox_file_path)
		print(self.instseg_file_path)
		# Read the ORIGINAL IMAGE and store it in the FIRST INDEX (i.e., 0) of the array
		self.image_data.append(cv2.imread(self.image_file_path))
		# We process the image and apply segmentation based on the bounding boxes given
		self.segment_image(file_name_prefix)

	def segment_image(self, file_name_prefix):
		original_image = self.image_data[0]
		self.image_data.append(np.copy(self.image_data[0]))
		with open(self.boundbox_file_path) as file:
			file_data = file.read()
			file_data_lines = [f for f in file_data.split("\n")]  # Try to convert this in a one line, don't write loop
			print(f"Total possible strawberries: {len(file_data_lines)}")
			# self.strawberries.append(Strawberry() for l in file_data_lines)
			for i, line in enumerate(file_data_lines):
				if line != "":
					self.strawberries.append(Strawberry())
					self.strawberries[i].create_bounding_box(line, self.image_data[0].shape)

		for strawberry in self.strawberries:
			sx, sy, ex, ey = strawberry.get_bounding_box().get_boundaries()
			self.image_data[1] = cv2.rectangle(self.image_data[1], (sx, sy), (ex, ey),
			                                   color=strawberry.get_class_color())
			strawberry.get_strawberry_image(self.image_data[0])
			strawberry.show_strawberry()

	def show_image(self, image_index=0):
		cv2.imshow(f"{self.file_name_prefix}", self.image_data[image_index])
		cv2.waitKey(0)
