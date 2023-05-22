import pdfplumber
from typing import Tuple

# Open the PDF file
with pdfplumber.open('./data/forms/ex.pdf') as pdf:
    # Extract text from specific coordinates
    page = pdf.pages[0]  # Select the desired page (e.g., page 1)
    print(page.height, page.width)
    x1, y1, x2, y2 = 100, 200, 300, 250  # Define the coordinates (top-left and bottom-right)
    text = page.crop(bbox=(100, 100, 300, 300)).extract_text()

# Print the extracted text
print(text)


class Point:
    def __init__(self, doc_height:float, doc_width:float):
        self.doc_height:float = doc_height
        self.doc_width:float = doc_width

    def convert_point(self, y:float, x:float, point: 'Point') -> Tuple[float, float]:
        x_new = x * (point.doc_width / self.doc_width)
        y_new = y * (point.doc_height / self.doc_height)
        return (x_new, y_new)

p1 = Point(11, 8.5)
p2 = Point(792, 612)
print(p1.convert_point(1.35, 1.33, p2))
print(p1.convert_point(3.81, 1.51, p2))