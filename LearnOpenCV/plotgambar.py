import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path = r'kucing.jpg'
img = cv.imread(path)

Red = img[:, :, 0]
Green = img[:, :, 2]
Blue = img[:, :, 1]
color = ('b', 'g', 'r')

height = img.shape[0]
width = img.shape[1]

grayscale = np.zeros([height, width], dtype=np.int32())

for row in range(1, height):
    for col in range(1, width):
        grayscale[row, col] = (0.299 * Red[row, col]) + \
            (0.587 * Green[row, col]) + (0.114 * Blue[row, col])

# Ubah Kontras
res = cv.convertScaleAbs(img, alpha=1.2, beta=0)

# plt.hist(img.ravel(), 256, [0, 256])

# Menampilkan Plot
for i, col in enumerate(color):
    histr = cv.calcHist([res], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

cv.imshow('Original', img)
cv.imshow('Grayscale', np.uint8(grayscale))
cv.imshow('Contrast', res)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows
