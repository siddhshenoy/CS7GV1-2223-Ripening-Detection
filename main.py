import os
import cv2
import numpy as np
from custom import Strawberry_Image

name_list = [str(i) for i in range(0, 3102)]


if __name__ == "__main__":
	si = Strawberry_Image.StrawberryImage()
	si.read_file("10")
	si.show_image()
	si.show_image(1)
# dir_list = os.listdir("./images")
# print(dir_list)
