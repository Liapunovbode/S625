from pdf2image import convert_from_path
import os

pdf_path = "S62522.pdf"
output_folder = "pages"

os.makedirs(output_folder, exist_ok=True)

pages = convert_from_path(pdf_path)

for i, page in enumerate(pages):
    page.save(f"{output_folder}/page_{i}.jpg", "JPEG")

print("PDF convertido")