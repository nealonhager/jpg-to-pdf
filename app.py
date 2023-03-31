import os
import glob
from PIL import Image
from fpdf import FPDF

# Get the path to the directory containing the JPEG files
path = input("Enter the path to the directory containing the JPEG files: ")

# Get the name of the directory
directory_name = os.path.basename(path)

# Create a new PDF file with the directory name as its filename
pdf = FPDF(unit="pt", format="letter")
pdf.set_title(directory_name)
pdf.set_author("Your Name")

# Get a list of all JPEG files in the directory
jpeg_files = glob.glob(os.path.join(path, "*.jpg"))

# Loop through each JPEG file, add it as a page to the PDF
for image in jpeg_files:
    # Open the image and get its dimensions
    with Image.open(image) as img:
        width, height = img.size

        # Calculate the scaling factor to fit the image within the PDF page
        pdf_width, pdf_height = pdf.w, pdf.h
        width_ratio = pdf_width / width
        height_ratio = pdf_height / height
        scale_factor = min(width_ratio, height_ratio)

        # Calculate the new dimensions of the image based on the scaling factor
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Calculate the position of the image on the page to center it
        x = (pdf_width - new_width) / 2
        y = (pdf_height - new_height) / 2

        # Add a new page to the PDF with the same dimensions as the page
        pdf.add_page()

        # Add the image to the page with black bars to maintain aspect ratio
        pdf.image(image, x, y, new_width, new_height)

# Save the PDF file in the same directory as the JPEG files
pdf.output(os.path.join(path, directory_name + ".pdf"), "F")
