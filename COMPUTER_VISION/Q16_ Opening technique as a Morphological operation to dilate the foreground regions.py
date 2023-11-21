import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for opening
kernel = np.ones((5,5), np.uint8)

# Apply the opening operation using cv2.morphologyEx() function
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Display the original and opened images
cv2.imshow("Original Image", img)
cv2.imshow("Opened Image", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
