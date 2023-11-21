import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for the black hat transform
kernel = np.ones((5, 5), np.uint8)

# Apply the black hat transform using cv2.morphologyEx() function
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display the original and black hat transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Black Hat Transformed Image", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
