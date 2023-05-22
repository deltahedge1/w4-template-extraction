from pdf2image import convert_from_path

# Path to the PDF file
pdf_path = './data/forms/ex2.pdf'

# Convert the first page of the PDF to an image
images = convert_from_path(pdf_path)

# Save the image
images[0].save('ex2.jpg', 'JPEG')