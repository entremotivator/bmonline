import io
import pandas as pd

def download_pdf(content, filename):
    """Generate a downloadable PDF."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

def download_csv(data, filename):
    """Generate a downloadable CSV."""
    output = io.BytesIO()
    df = pd.DataFrame(data)
    df.to_csv(output, index=False)
    output.seek(0)
    return output
