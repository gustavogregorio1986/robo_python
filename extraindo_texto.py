import pypdf

leitor = pypdf.PdfWriter("o_cortico.pdf")

print(leitor.pages[0].extract_text())