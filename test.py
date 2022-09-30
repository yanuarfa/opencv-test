import cv2

path=r'D:\kucing.jpg'; #https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2021/10/28064854/12.-Tips-Merawat-Anak-Kucing-Munchkin.jpg
cv_read=cv2.imread(path);
height=cv_read.shape[0];
width=cv_read.shape[1];
dimension=cv_read.shape[2];
cv2.imshow("ini kucing",cv_read);

pixels=cv_read[0][0];

cv2.waitKey(0);
cv2.destroyAllWindows;
