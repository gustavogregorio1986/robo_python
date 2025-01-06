import pypdf

leitor = pypdf.PdfReader("o_cortico.pdf")

for pagina in leitor.pages:
 for imagem in leitor.pages[0].images:
    with open(f'imagens/{imagem.name}','wb') as file:
        file.write(imagem.data)