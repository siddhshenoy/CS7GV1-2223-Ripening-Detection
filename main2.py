import cv2

img = cv2.imread("./images/10.png")
cv2.imshow("original", img)
cv2.imshow("bounding", cv2.rectangle(img,  (433, 240),(543,396), color=(0,0, 255)))
cv2.imshow("crop", img[240:396, 433: 543])
cv2.waitKey(0)

