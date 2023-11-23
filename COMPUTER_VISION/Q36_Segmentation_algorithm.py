import cv2

# Load the input image
image = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the grayscale image
_, thresholded_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
