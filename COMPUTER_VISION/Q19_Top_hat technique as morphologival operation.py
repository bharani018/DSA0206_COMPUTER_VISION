import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for the top-hat transform
kernel = np.ones((5, 5), np.uint8)

# Apply the top-hat transform using cv2.morphologyEx() function
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the original and top-hat transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Top-Hat Transformed Image", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
