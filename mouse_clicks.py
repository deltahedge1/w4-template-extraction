import cv2

# List to store the rectangles
rectangles = []
current_rectangle = []

# Callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    global current_rectangle

    if event == cv2.EVENT_LBUTTONDOWN:
        # Start a new rectangle
        current_rectangle = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        # Add the completed rectangle to the list
        current_rectangle.append((x, y))
        rectangles.append(tuple(current_rectangle))
        current_rectangle = []

        # Print the coordinates of the rectangle
        if len(current_rectangle) == 2:
            print(f"Rectangle: Top-left: {current_rectangle[0]}, Bottom-right: {current_rectangle[1]}")

# Load the image
image = cv2.imread('image.jpg')

# Create a named window to display the image
cv2.namedWindow('Image')

# Set the callback function for mouse events
cv2.setMouseCallback('Image', mouse_callback)

# Display the image
while True:
    # Draw the rectangles on the image
    image_copy = image.copy()
    for rectangle in rectangles:
        cv2.rectangle(image_copy, rectangle[0], rectangle[1], (0, 255, 0), 2)

    cv2.imshow('Image', image_copy)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit
    if key == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()
