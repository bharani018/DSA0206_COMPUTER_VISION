import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for closing
kernel = np.ones((5,5), np.uint8)

# Apply the closing operation using cv2.morphologyEx() function
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display the original and closed images
cv2.imshow("Original Image", img)
cv2.imshow("Closed Image", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
