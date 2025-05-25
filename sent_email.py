import smtplib
from email.message import EmailMessage
import os

def enviar_email_com_anexo(destinatario, arquivo_pdf):
    EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM")
    EMAIL_SENHA = os.getenv("EMAIL_SENHA_APP")

    msg = EmailMessage()
    msg["Subject"] = "Seu Plano de Treino Personalizado 🏃"
    msg["From"] = EMAIL_ORIGEM
    msg["To"] = destinatario
    msg.set_content("Olá! Segue em anexo o seu plano de treino gerado com base nas informações do formulário.")

    # Anexa o PDF
    with open(arquivo_pdf, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=arquivo_pdf)

    # Envia
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ORIGEM, EMAIL_SENHA)
        smtp.send_message(msg)
