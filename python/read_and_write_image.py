import cv2


img_unchanged = cv2.imread("images/rose.jpeg", cv2.IMREAD_UNCHANGED)
img_grayscale = cv2.imread("images/rose.jpeg", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("images/rose.jpeg", cv2.IMREAD_COLOR)

cv2.imshow("unchanged image", img_unchanged)
cv2.imshow("grayscale image", img_grayscale)
cv2.imshow("color image", img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("images/grayscale.jpg", img_grayscale)
