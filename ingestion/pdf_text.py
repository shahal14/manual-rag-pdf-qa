import fitz  # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    results = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            results.append({
                "type": "text",
                "content": text,
                "page": page_num + 1
            })
    return results
