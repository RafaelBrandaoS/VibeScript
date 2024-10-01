import os
import re
from openai import OpenAI
from dotenv import load_dotenv

def enviarParaGPT(caracteristicas, msgUsuario):
    load_dotenv()
    CHAVE_API = os.getenv('API_OPENAI')

    client = OpenAI(api_key=CHAVE_API)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Finja que você é um roteirista profissional e tem ue fazer um roteiro para um víodeo de 2 minutos, em primeira pessoa para uma pessoa com as seguintes características: {caracteristicas}. Quero a resposta separada em cenas e seja formatada em Markdown."},
            {"role": "user", "content": f"Gere um roteiro com o seguinte tema: {msgUsuario}"}
        ]
    )

    resposta = response.choices[0].message.content
    
    resposta = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', resposta)
    resposta = re.sub(r'(^|\n)# (.+)', r'<h2>\2</h2>', resposta)
    resposta = re.sub(r'(^|\n)## (.+)', r'<h3>\2</h3>', resposta)
    resposta = re.sub(r'(^|\n)### (.+)', r'<h3>\2</h3>', resposta)
    resposta = re.sub(r'(^|\n)#### (.+)', r'<h3>\2</h3>', resposta)

    resposta = resposta.replace('--', '<hr>')
    resposta = resposta.replace('---', '<hr>')
    
    resposta = resposta.replace('\n', '<br><br>')

    print(resposta)

    return resposta
