from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

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
    pdf.cell(0, 10, "Experiência Profissional:", ln=True)
    pdf.set_font("Arial", "", 12)
    for exp in experiencia:
        pdf.cell(0, 8, f"- {exp.strip()}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Formação Acadêmica:", ln=True)
    pdf.set_font("Arial", "", 12)
    for edu in educacao:
        pdf.cell(0, 8, f"- {edu.strip()}", ln=True)

    pdf_path = "curriculo.pdf"
    pdf.output(pdf_path)
    return pdf_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    habilidades = request.form['habilidades'].split(',')
    experiencia = request.form['experiencia'].split(',')
    educacao = request.form['educacao'].split(',')

    pdf_path = gerar_curriculo(nome, email, telefone, habilidades, experiencia, educacao)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
