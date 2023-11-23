import cv2

# Load the input image
image = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Apply the Sobel filter to the image
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, 3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, 3)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
