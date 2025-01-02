import pypdf
from PyPDF2 import PdfReader, PdfWriter

# lendo o arquivo
arquivo_pdf = pypdf.PdfReader("o_cortico.pdf")

# Escrever  um PDF

pdf_destino = pypdf.PdfWriter()


# Niumero de paginas do PDF
print(arquivo_pdf.pages)

len(arquivo_pdf.pages)

print(arquivo_pdf.pages[0])

for pagina in arquivo_pdf.pages:
    print(pagina)

# metodos de um PDF
print(arquivo_pdf.metadata)

# extraindo uma pagina PDF
from PyPDF2 import PdfReader, PdfWriter

# Carregar o arquivo PDF de origem
caminho_pdf_origem = "caminho_para_seu_arquivo.pdf"  # Substitua pelo caminho do seu arquivo PDF
leitor_pdf = PdfReader(caminho_pdf_origem)

# Criar um objeto PdfWriter para o novo arquivo
escritor_pdf = PdfWriter()

# Selecionar a primeira página
primeira_pagina = leitor_pdf.pages[0]
escritor_pdf.add_page(primeira_pagina)

# Salvar a página extraída em um novo arquivo
caminho_pdf_destino = "Pagina-01.pdf"
with open(caminho_pdf_destino, "wb") as arquivo_saida:
    escritor_pdf.write(arquivo_saida)

print(f"Página extraída com sucesso para {caminho_pdf_destino}")

