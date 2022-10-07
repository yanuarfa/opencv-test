import numpy as np
import cv2 as cv

vid = cv.VideoCapture('people.mp4')
# print(vid)

while vid.isOpened():
    ret, frame = vid.read()

    if not ret:
        print("Tidak bisa mendapatkan frame (stream end?). Exiting...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

vid.release()
cv.destroyAllWindows()