def gerar_curriculo(nome, email, telefone, habilidades, experiencia, educacao):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Curriculo Profissional", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Nome: {nome}", ln=True)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Telefone: {telefone}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Habilidades:", ln=True)
    pdf.set_font("Arial", "", 12)
    for habilidade in habilidades:
        pdf.cell(0, 8, f"- {habilidade.strip()}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Experiencia Profissional:", ln=True)
    pdf.set_font("Arial", "", 12)
    for exp in experiencia:
        pdf.cell(0, 8, f"- {exp.strip()}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Formacao Academica:", ln=True)
    pdf.set_font("Arial", "", 12)
    for edu in educacao:
        pdf.cell(0, 8, f"- {edu.strip()}", ln=True)
    
    pdf_path = "curriculo.pdf"
    pdf.output(pdf_path)
    return pdf_path
