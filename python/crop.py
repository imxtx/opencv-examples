import cv2


# read image
img = cv2.imread("images/rose.jpeg")
cv2.imshow(f"original size: {img.shape}", img)

# crop the image by slicing the internal numpy array
# note: the first axis is row, the second axis is column.
#       y range: [150,700), x range: [240,780)
cropped = img[150: 700, 240:780]
cv2.imshow(f"cropped size: {cropped.shape}", cropped)

# save
cv2.imwrite("images/rose_cropped.jpg", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
