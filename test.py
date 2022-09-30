import cv2

path=r'D:\kucing.jpg';
cv_read=cv2.imread(path);
cv2.imshow("ini kucing",cv_read);

cv2.waitKey(0);
cv2.destroyAllWindows;
