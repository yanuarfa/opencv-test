import numpy as np
import cv2 as cv

vid = cv.VideoCapture('people.mp4')
# print(vid)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while vid.isOpened():
    ret, frame = vid.read()

    if not ret:
        print("Tidak bisa mendapatkan frame (stream end?). Exiting...")
        break

    # frame = cv.flip(frame, 0) # Memutar video 180 derajat

    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

vid.release()
out.release()
cv.destroyAllWindows()