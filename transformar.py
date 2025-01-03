import pypdf

pdf = pypdf.PdfWriter(clone_from="o_cortico.pdf")

transformacao = pypdf.Transformation()

pdf.pages[0].add_transformation(transformacao.rotate(50))

pdf.write("PDF Transformacao.pdf")