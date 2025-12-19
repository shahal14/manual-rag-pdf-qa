import fitz
import pytesseract
from PIL import Image
import io

def extract_images_ocr(pdf_path):
    doc = fitz.open(pdf_path)
    results = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            image = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(image)

            if text.strip():
                results.append({
                    "type": "image_ocr",
                    "content": text,
                    "page": page_index + 1
                })
    return results
