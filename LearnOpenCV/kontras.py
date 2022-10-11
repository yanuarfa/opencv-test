import cv2 as cv
import matplotlib.pyplot as plt

path = r'kucing.jpg'
img = cv.imread(path)

res = cv.convertScaleAbs(img, alpha=1.2, beta=0)

cv.imshow('Original', img)
cv.imshow('Contrast', res)
cv.waitKey(0)
cv.destroyAllWindows
