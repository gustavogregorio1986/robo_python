from PyPDF2 import PdfReader, PdfWriter

# Abrir o PDF existente
reader = PdfReader("o_cortico.pdf")
writer = PdfWriter()

# Copiar páginas do PDF original para o Writer
for page in reader.pages:
    writer.add_page(page)

# Ler o arquivo para anexar
with open("coxinha.jpg", "rb") as file:
    arquivo = file.read()

# Adicionar o anexo ao PDF
writer.add_attachment("coxinha.jpg", arquivo)

# Salvar o PDF com o anexo
with open("o_cortico_anexo.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("PDF criado com sucesso!")
