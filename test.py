import cv2

path=r'D:\kucing.jpg'; #https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2021/10/28064854/12.-Tips-Merawat-Anak-Kucing-Munchkin.jpg
cv_read=cv2.imread(path);
cv2.imshow("ini kucing",cv_read);

cv2.waitKey(0);
cv2.destroyAllWindows;
