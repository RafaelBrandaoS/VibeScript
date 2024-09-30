import os
from openai import OpenAI
from dotenv import load_dotenv

def enviarParaGPT(caracteristicas, msgUsuario):
    load_dotenv()
    CHAVE_API = os.getenv('API_OPENAI')

    client = OpenAI(api_key=CHAVE_API)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Finja que você é um roteirista profissional e tem ue fazer um roteiro para um víodeo de 1 minutos para uma pessoa com as seguintes características: {caracteristicas}"},
            {"role": "user", "content": f"Gere um roteiro com o seguinte tema: {msgUsuario}"}
        ]
    )

    print(response)

    return response.choices[0].message.content
