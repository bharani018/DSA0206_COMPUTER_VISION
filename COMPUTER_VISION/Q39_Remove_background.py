import cv2
import numpy as np

# Read the input image
image_path = "C:/Users/HP/OneDrive/Pictures/computer_vision_images/man.jpg"
image = cv2.imread(image_path)

# Convert the image from BGR to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the background color range (adjust as needed)
lower_bound = np.array([200, 200, 200], dtype=np.uint8)
upper_bound = np.array([255, 255, 255], dtype=np.uint8)

# Create a mask for pixels within the specified color range
mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

# Set the pixels in the mask to black (remove the background)
image_without_background = cv2.bitwise_and(image_rgb, image_rgb, mask=~mask)

# Display the original and processed images
cv2.imshow('Original Image', image_rgb)
cv2.imshow('Image without Background', image_without_background)
cv2.waitKey(0)
cv2.destroyAllWindows()
