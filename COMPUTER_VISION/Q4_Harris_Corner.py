import cv2
import numpy as np

# Function to perform Harris Corner Detection
def detect_corners(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Check if the image is loaded successfully
    if img is None:
        print("Error: Unable to load the image.")
        exit()

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect corners using Harris Corner Detection
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Dilate corners to make them more visible
    corners = cv2.dilate(corners, None)

    # Threshold for an optimal value, it may vary depending on the image
    threshold = 0.01 * corners.max()

    # Mark the corners on the image
    img[corners > threshold] = [0, 0, 255]  # Red color for corners

    # Display the result
    cv2.imshow('Corners Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Provide the path to your image
image_path = "C:/Users/HP/OneDrive/Pictures/computer_vision_images/img_3.jpeg"
# Call the function to detect corners
detect_corners(image_path)
