import pypdf

# lendo o arquivo
arquivo_pdf = pypdf.PdfReader("o_cortico.pdf")

# Niumero de paginas do PDF
print(arquivo_pdf.pages)

len(arquivo_pdf.pages)

print(arquivo_pdf.pages[0])

for pagina in arquivo_pdf.pages:
    print(pagina)

# metodos de um PDF
print(arquivo_pdf.metadata)