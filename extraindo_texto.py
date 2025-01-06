import pypdf

leitor = pypdf.PdfWriter("o_cortico.pdf")

print(leitor.pages[0].extract_text())

textos = []
for pagina in leitor.pages:
    textos.append(pagina.extract_text())


texto = ''.join(textos)

print(texto)
