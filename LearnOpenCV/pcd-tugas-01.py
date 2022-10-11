import cv2 as cv
# import numpy as np
import matplotlib.pyplot as plt

path = r'kucing.jpg'
img = cv.imread(path)
color = ('b', 'g', 'r')

# Ubah Kontras
res = cv.convertScaleAbs(img, alpha=1.2, beta=0)

# plt.hist(img.ravel(), 256, [0, 256])

# Menampilkan Plot
for i, col in enumerate(color):
    histr = cv.calcHist([res], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

cv.imshow('Original', img)
cv.imshow('Contrast', res)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows
