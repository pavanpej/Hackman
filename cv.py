#!usr/bin/python
import cv2
import numpy
import matplotlib as plt

img = cv2.imread('Wolverine.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()