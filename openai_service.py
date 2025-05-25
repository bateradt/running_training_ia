import openai
import os

def post_prompt_ai_training(dados: dict) -> str:
    # key for openrouter.ai
    key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=key
    )

    prompt = f"""
    Monte um plano de treino para:
    - Nome: {dados['name']}
    - Idade: {dados['age']}
    - Peso: {dados['weight']}
    - Frequência: {dados['weekFrequency']} vezes por semana
    - Dias disponíveis: {', '.join(dados['availableDays'])}
    - Distância atual: {dados['currentDistance']}
    - Distância alvo: {dados['targetDistance']}
    - Pace alvo: {dados['targetPace']}
    - Data da prova: {dados['raceDate']}
    - Data de início do treino: {dados['startDate']}
    O plano deve conter sugestões semanais de treinos com progressão gradual até a data da prova.
    """

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-maverick:free",
            messages=[
                {"role": "system", "content": "Você é um especialista em corrida e criação de planilhas de treino."},
                {"role": "user", "content": prompt}
            ]
        )
    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)  # an underlying Exception, likely raised within httpx.
    except openai.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
        print(e.response)
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)

    treino = response.choices[0].message.content
    return treino