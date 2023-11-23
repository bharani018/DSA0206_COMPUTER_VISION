import cv2
import numpy as np

def create_white_image_with_circle(size, circle_center, circle_radius):
    # Create a white image
    white_image = np.full((size, size, 3), 255, dtype=np.uint8)

    # Draw a circle on the white image
    cv2.circle(white_image, circle_center, circle_radius, (0, 0, 0), -1)

    # Display the image with the circle
    cv2.imshow('White Image with Circle', white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Prompt the user to enter the size, circle center, and circle radius
size = int(input("Enter the size of the image: "))
circle_center = (int(input("Enter the x-coordinate of the circle center: ")), int(input("Enter the y-coordinate of the circle center: ")))
circle_radius = int(input("Enter the radius of the circle: "))

# Call the function with the user-provided inputs
create_white_image_with_circle(size, circle_center, circle_radius)
