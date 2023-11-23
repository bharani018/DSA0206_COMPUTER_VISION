import cv2
import numpy as np

# Load the input image
image = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Define the translation matrix
translation_matrix = np.float32([[1, 0, 25], [0, 1, 25]])

# Translate the image using the translation matrix
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Display the original and translated images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
