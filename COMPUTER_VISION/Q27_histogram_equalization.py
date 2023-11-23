import cv2

# Read the input image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
equalized = cv2.equalizeHist(gray)

# Display the original and equalized images
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equalized)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
