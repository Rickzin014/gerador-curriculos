from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

def gerar_curriculo(nome, email, telefone, habilidades, experiencia, educacao):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Cores e fontes
    azul = (30, 144, 255)
    preto = (0, 0, 0)

    # Cabeçalho
    pdf.set_font("Arial", "B", 20)
    pdf.set_text_color(*azul)
    pdf.cell(0, 10, nome, ln=True, align='C')

    pdf.set_font("Arial", "", 14)
    pdf.set_text_color(*preto)
    pdf.cell(0, 10, "Currículo Profissional", ln=True, align='C')
    pdf.ln(5)

    # Contato
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"📧 {email}   📱 {telefone}", ln=True, align='C')
    pdf.ln(10)

    def add_secao(titulo, lista):
        pdf.set_text_color(*azul)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"🔹 {titulo}", ln=True)
        pdf.set_text_color(*preto)
        pdf.set_font("Arial", "", 12)
        for item in lista:
            pdf.multi_cell(0, 8, f"- {item.strip()}")
        pdf.ln(5)

    add_secao("Habilidades", habilidades)
    add_secao("Experiência Profissional", experiencia)
    add_secao("Formação Acadêmica", educacao)

    # Linha final
    pdf.set_draw_color(*azul)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # Salvar PDF
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
