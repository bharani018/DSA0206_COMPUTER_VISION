import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for morphological gradient
kernel = np.ones((5,5), np.uint8)

# Apply the morphological gradient operation using cv2.morphologyEx() function
morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Display the original and morphological gradient images
cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient Image", morph_gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
