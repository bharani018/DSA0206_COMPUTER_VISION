import cv2
import numpy as np

def create_white_image_with_boxes():
    # Get size of the image from the user
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Create a white image of the specified size
    img = np.ones((height, width, 3), np.uint8) * 255

    # Draw four boxes on the image
    box_size = int(min(width, height) / 10)  # Size of the colored boxes
    thickness = -1  # Fill the boxes by the specified color

    # Draw black box on the top-left corner
    start_point = (0, 0)
    end_point = (box_size, box_size)
    color = (0, 0, 0)  # BGR color format (blue, green, red)
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Draw blue box on the top-right corner
    start_point = (width - box_size, 0)
    end_point = (width, box_size)
    color = (255, 0, 0)  # BGR color format (blue, green, red)
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Draw green box on the bottom-left corner
    start_point = (0, height - box_size)
    end_point = (box_size, height)
    color = (0, 255, 0)  # BGR color format (blue, green, red)
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Draw red box on the bottom-right corner
    start_point = (width - box_size, height - box_size)
    end_point = (width, height)
    color = (0, 0, 255)  # BGR color format (blue, green, red)
    cv2.rectangle(img, start_point, end_point, color, thickness)

    # Display the image
    cv2.imshow("White Image with Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function to create the white image with four boxes
create_white_image_with_boxes()
