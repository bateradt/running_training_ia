def gerar_html_treino(nome, distancia, data_prova, plano_treino_texto):
    """
    Gera um HTML estruturado para o plano de treino.
    
    plano_treino_texto: texto gerado pela IA, separado por quebras de linha (\n)
    """
    treino_formatado = "".join(
        f"<p>{linha}</p>" for linha in plano_treino_texto.strip().split("\n") if linha.strip()
    )

    html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Plano de Treino - {nome}</title>
            <style>
                body {{
                    font-family: 'Helvetica', sans-serif;
                    margin: 40px;
                    color: #333;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                }}
                h1 {{
                    text-align: center;
                    color: #007BFF;
                }}
                .meta {{
                    background: #f1f1f1;
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                }}
                .meta p {{
                    margin: 5px 0;
                }}
                .treino {{
                    line-height: 1.6;
                }}
                footer {{
                    text-align: center;
                    margin-top: 40px;
                    font-size: 0.9em;
                    color: #888;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Plano de Treino Personalizado</h1>
                <div class="meta">
                    <p><strong>Atleta:</strong> {nome}</p>
                    <p><strong>Distância Alvo:</strong> {distancia}</p>
                    <p><strong>Data da Prova:</strong> {data_prova}</p>
                </div>
                <div class="treino">
                    {treino_formatado}
                </div>
                <footer>
                    Gerado automaticamente por IA – Projetos de Corrida 2025 🏃‍♂️
                </footer>
            </div>
        </body>
        </html>
        """
    return html