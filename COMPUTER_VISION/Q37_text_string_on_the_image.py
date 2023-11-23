import numpy as np
import cv2

# Create a white image
image = np.ones((150, 200, 3), dtype=np.uint8) * 255

# Get user input for the text string
user_text = input("Enter the text to be displayed: ")

# Define font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)
font_thickness = 2

# Get text size to calculate text position
text_size = cv2.getTextSize(user_text, font, font_scale, font_thickness)[0]
text_position = ((image.shape[1] - text_size[0]) // 2, (image.shape[0] + text_size[1]) // 2)

# Put the text on the image
cv2.putText(image, user_text, text_position, font, font_scale, font_color, font_thickness)

# ... (previous code)

# Display the image for 5 seconds (5000 milliseconds)
cv2.imshow('Image with Text', image)
cv2.waitKey(00)

# Close all windows
cv2.destroyAllWindows()
