import camelot


def extract_tables(pdf_path):
    """
    Extract tables from a PDF using Camelot.
    Returns tables as text blocks with page numbers.
    """
    results = []

    try:
        tables = camelot.read_pdf(pdf_path, pages="all")
    except Exception as e:
        print(f"[WARN] Camelot failed: {e}")
        return results

    for table in tables:
        results.append({
            "type": "table",
            "content": table.df.to_string(index=False),
            "page": table.page
        })

    return results
