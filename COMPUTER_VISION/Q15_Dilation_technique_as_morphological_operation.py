import cv2
import numpy as np

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg", 0)

# Define the kernel for dilation
kernel = np.ones((5,5), np.uint8)

# Apply the dilation operation using cv2.dilate() function
dilation = cv2.dilate(img, kernel, iterations=1)

# Display the original and dilated images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
