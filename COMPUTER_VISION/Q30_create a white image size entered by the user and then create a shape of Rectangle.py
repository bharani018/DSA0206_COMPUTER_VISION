import cv2
import numpy as np

def create_white_image_with_rectangle():
    # Get size of the image from the user
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Create a white image of the specified size
    img = np.ones((height, width, 3), np.uint8) * 255

    # Draw a rectangle on the image
    start_point = (50, 50)
    end_point = (200, 200)
    color = (0, 0, 255)  # BGR color format (blue, green, red)
    thickness = 2
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Display the image
    cv2.imshow("White Image with Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function to create the white image with a rectangle
create_white_image_with_rectangle()
