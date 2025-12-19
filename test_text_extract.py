print("🚀 test_text_extract.py started")

from ingestion.pdf_text import extract_text
import os

pdf_path = "data/raw_docs/sample.pdf"

print("📄 PDF path:", pdf_path)
print("📂 PDF exists:", os.path.exists(pdf_path))

result = extract_text(pdf_path)

print("📊 Number of extracted text chunks:", len(result))

if result:
    print("🧾 First chunk preview:")
    print(result[0]["content"][:500])
else:
    print("⚠️ No text extracted from the PDF")
