import cv2
import numpy as np

# Load the input image
image = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/man.jpg")

# Create a background subtractor with MOG2 algorithm
fgbg = cv2.createBackgroundSubtractorMOG2()

# Convert the input image to a 1-dimensional array for background subtraction
image_1d = image.flatten()

# Apply the background subtractor to the input image
result = fgbg.apply(image_1d)

# Convert the result back to a 2-dimensional array
result = result.reshape(image.shape)

# Display the original and subtracted images
cv2.imshow('Original Image', image)
cv2.imshow('Subtracted Image', result)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
