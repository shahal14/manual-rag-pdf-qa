from ingestion.pdf_text import extract_text
from ingestion.pdf_tables import extract_tables

# OCR is optional
try:
    from ingestion.pdf_images_ocr import extract_images_ocr
except ImportError:
    extract_images_ocr = None



def ingest(pdf_path):
    """
    Run full multi-modal ingestion:
    text + tables + image OCR
    """
    data = []

    try:
        data.extend(extract_text(pdf_path))
    except Exception as e:
        print(f"[WARN] Text extraction failed: {e}")

    try:
        data.extend(extract_tables(pdf_path))
    except Exception as e:
        print(f"[WARN] Table extraction failed: {e}")
    if extract_images_ocr:
        try:
            data.extend(extract_images_ocr(pdf_path))
        except Exception as e:
            print(f"[WARN] OCR extraction failed: {e}")
    else:
        print("[INFO] OCR module not available, skipping OCR")


    return data
