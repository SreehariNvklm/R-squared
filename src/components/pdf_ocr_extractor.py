import pymupdf
import glob
import os
import pytesseract

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
    def extract_text(self):
        pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
        text_counter = 0
        for image_folder in glob.glob("output_images/*"):
            os.makedirs("output_text/" + str(text_counter),exist_ok=True)
            for text_file in glob.glob(image_folder + "/*.png"):
                text = pytesseract.image_to_string(text_file)
                with open(f"output_text/{text_counter}/text_{text_counter}.txt","w") as f:
                    f.write(text)
                print(f"Extracted text from: {text_file}")
            text_counter += 1
        
pdf_ocr = PDF_OCR_Extractor("output/output/*.pdf")
pdf_ocr.extract_text()