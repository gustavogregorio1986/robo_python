import pypdf

pdf = pypdf.PdfWriter(clone_from="o_cortico.pdf")

transformacao = pypdf.Transformation()

# rotacionar o conteudo
pdf.pages[0].add_transformation(transformacao
                                  .rotate(50)
                                  .translate(tx=400))


# movimentar o conteudo
pdf.pages[1].add_transformation(transformacao.translate(tx=400, ty=500))

pdf.pages[2].add_transformation(transformacao.scale(sx=0.5, sy=0.8))

#alterar a escala da paigna
pdf.pages[3].scale_by(1.5)

pdf.write("PDF Transformacao.pdf")

