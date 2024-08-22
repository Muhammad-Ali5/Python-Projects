from pdf2image import convert_from_path

# Define the paths
pdf_path = r"E:\python Programs\projects.py\Pdf to image\WebDev Roadmap - Notes.pdf"
poppler_path = r"E:\python Programs\projects.py\Pdf to image\poppler-24.07.0\Library\bin"

try:
    # Convert PDF to images
    old_pdf = convert_from_path(pdf_path, poppler_path=poppler_path)

    # Save each page as a separate JPEG file
    for i in range(len(old_pdf)):
        old_pdf[i].save("new_" + str(i) + '.jpg', 'JPEG')

    print("PDF conversion to images was successful!")

except FileNotFoundError as e:
    print(f"FileNotFoundError: The file was not found. {e}")
except Exception as e:
    print(f"An error occurred: {e}")
