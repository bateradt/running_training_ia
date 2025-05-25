from flask import Flask, request, jsonify
import uuid
from dotenv import load_dotenv
from create_pdf import gerar_pdf_com_xhtml2pdf
from generate_html import gerar_html_treino
from sent_email import enviar_email_com_anexo
from openai_service import post_prompt_ai_training

app = Flask(__name__)

load_dotenv()

@app.route("/running/training/model", methods=["POST"])
def trainning_model():
    try:
        dados = request.get_json()
        nome_pdf = f"treino_{uuid.uuid4().hex}.pdf"
        treino = post_prompt_ai_training(dados)
        html = gerar_html_treino(
                nome=dados['name'],
                distancia=dados['targetDistance'],
                data_prova=dados['raceDate'],
                plano_treino_texto=treino
                )
        gerar_pdf_com_xhtml2pdf(html, nome_pdf)
        enviar_email_com_anexo(dados['email'], nome_pdf)

        return jsonify({"status": "sucesso", "treino": treino, "pdf": nome_pdf}), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)