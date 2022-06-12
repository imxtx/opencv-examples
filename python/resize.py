import cv2

# Ref: https://learnopencv.com/image-resizing-with-opencv/

image = cv2.imread("images/rose.jpeg")

# resize with new with and new height
new_size = [800, 800]
resized1 = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)

# resize using scaling factors
resized2 = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized 1", resized1)
cv2.imshow("Resized 2", resized2)
cv2.waitKey(0)
cv2.destroyAllWindows()
