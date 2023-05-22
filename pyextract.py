import cv2
import pytesseract

# Load the image and specify the bounding coordinates
image = cv2.imread('ex2_Page_1.png')
points = [
    (261, 233, 759, 299), # Example bounding coordinates
    (757, 233, 1314, 299),
    (262, 300, 1316, 365),
    (261, 368, 1319, 433)
]

checkboxes = [
    (314, 433, 343, 460),
    (309, 466, 343, 496),
    (309, 496, 343, 529)
]

for point in points:
    x0, y0, x1, y1 = point
    roi = image[y0:y1, x0:x1]

    # Convert the region of interest to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Perform text extraction using pytesseract
    extracted_text = pytesseract.image_to_string(gray)

    # Print the extracted text
    print(extracted_text)