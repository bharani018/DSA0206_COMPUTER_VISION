import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Define the points for the input image and the corresponding points for the output image
pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])
pts2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])

# Compute the perspective transform matrix M using cv2.getPerspectiveTransform(pts1, pts2) function
M = cv2.getPerspectiveTransform(pts1, pts2)

# Transform the image using cv2.warpPerspective() method
dst = cv2.warpPerspective(img, M, (400, 640))

# Display the transformed image
cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
