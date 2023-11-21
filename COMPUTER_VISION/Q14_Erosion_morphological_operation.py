import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for erosion
kernel = np.ones((5,5), np.uint8)

# Apply the erosion operation using cv2.erode() function
erosion = cv2.erode(img, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
