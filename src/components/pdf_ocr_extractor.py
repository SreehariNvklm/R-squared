import pytesseract
import pymupdf
import glob
import os

pdf_files = glob.glob('output/output/*.pdf')

img_counter = 0
for pdf_file in pdf_files:
    os.makedirs("output_images/" + str(img_counter),exist_ok=True)
    doc = pymupdf.open(os.path.join(pdf_file))
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap()
        img_path = f"output_images/{img_counter}/page_{page_num + 1}.png"
        pix.save(img_path)
        print(f"Saved: {img_path}")
    img_counter += 1
