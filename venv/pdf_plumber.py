import pdfplumber

pdf = pdfplumber.open("sebrae.pdf")

texto = pdf.pages[18].extract_text()

print(texto)

tabela = pdf.pages[29].extract_table()

tabelas = pdf.pages[29].extract_tables()

print(tabela[0])

print(tabela[1])