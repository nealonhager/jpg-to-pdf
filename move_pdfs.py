import os
import shutil

# Get the path to the parent directory containing subfolders with PDF files
parent_directory = input(
    "Enter the path to the parent directory containing subfolders with PDF files: "
)

# Loop through each subfolder and move all PDF files to the parent directory
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        # Check if the file is a PDF file
        if file.endswith(".pdf"):
            # Get the full path to the PDF file
            pdf_path = os.path.join(root, file)

            # Move the PDF file to the parent directory
            shutil.move(pdf_path, os.path.join(parent_directory, file))
