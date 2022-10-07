import cv2
import numpy as np

path=r'D:\kucing.jpg'; #https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2021/10/28064854/12.-Tips-Merawat-Anak-Kucing-Munchkin.jpg
cv_read=cv2.imread(path)
cv2.imshow("Citra RGB",cv_read)

Red = cv_read[:,:,0]
Green = cv_read[:,:,2]
Blue = cv_read[:,:,1]

height = cv_read.shape[0]
width = cv_read.shape[1]
constant_value = np.int32(50)

grayscale = np.zeros([height, width], dtype = np.int32())
gray_bright = np.zeros([height, width], dtype = np.int32())

for row in range (1, height):
    for col in range (1, width):
        grayscale[row, col] = (0.299 * Red[row, col]) + (0.587 * Green[row, col]) + (0.114 * Blue[row, col])
        gray_bright[row, col] = grayscale[row, col] + constant_value

cv2.imshow('Grayscale', np.uint8(grayscale))
cv2.imshow('Grayscale Bright', np.uint8(gray_bright))
cv2.waitKey(0)
cv2.destroyAllWindows