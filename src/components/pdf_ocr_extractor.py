import pytesseract
import pymupdf
import glob
import os

class PDF_OCR_Extractor:
    def __init__(self,pdf_path):
        self.pdf_path = glob.glob(pdf_path)
    def extract_imgs(self):
        img_counter = 0
        for pdf_file in self.pdf_path:
            os.makedirs("output_images/" + str(img_counter),exist_ok=True)
            self.doc = pymupdf.open(pdf_file)
            for page_num in range(len(self.doc)):
                page = self.doc[page_num]
                pix = page.get_pixmap()
                img_path = f"output_images/{img_counter}/page_{page_num + 1}.png"
                pix.save(img_path)
                print(f"Saved: {img_path}")
            img_counter += 1

pdf_ocr = PDF_OCR_Extractor("output/output/*.pdf")
pdf_ocr.extract_imgs()