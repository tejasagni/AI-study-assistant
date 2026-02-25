from fpdf import FPDF

def create_report(name, insight):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)
    pdf.cell(200,10,txt="Student Study Report", ln=True, align="C")

    pdf.ln(10)
    pdf.cell(200,10,txt=f"Student: {name}", ln=True)
    pdf.multi_cell(0,10,txt=f"Feedback: {insight}")

    file_name = f"{name}_report.pdf"
    pdf.output(file_name)
    return file_name