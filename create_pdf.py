from xhtml2pdf import pisa

def gerar_pdf_com_xhtml2pdf(html_content, nome_arquivo_pdf):
    with open(nome_arquivo_pdf, "wb") as f:
        pisa_status = pisa.CreatePDF(html_content, dest=f)
    if pisa_status.err:
        print("Erro ao gerar PDF")
    else:
        print(f"PDF salvo como {nome_arquivo_pdf}")