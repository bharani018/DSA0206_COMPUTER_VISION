import cv2

# Load the input image
image = cv2.imread("C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg")

# Convert the image from BGR to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and converted images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
