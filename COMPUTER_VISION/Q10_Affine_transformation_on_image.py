import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Define the points for the input image and the corresponding points for the output image
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

# Compute the affine transform matrix M using cv2.getAffineTransform(pts1, pts2) function
M = cv2.getAffineTransform(pts1, pts2)

# Transform the image using cv2.warpAffine() method
rows, cols, ch = img.shape
dst = cv2.warpAffine(img, M, (cols, rows))

# Display the transformed image
cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
