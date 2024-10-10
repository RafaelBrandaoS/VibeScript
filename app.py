from flask import render_template
from login.login import login_bp
from registrar.registrar import registrar_bp
from plataforma.plataforma import plataforma_bp
from extencoes import criar_app


app = criar_app()

app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(registrar_bp, url_prefix='/registrar')
app.register_blueprint(plataforma_bp, url_prefix='/plataforma')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
    PRÓXIMOS PASSOS PARA O VIBESCRIPT
    c   CORRIGIR ERRO DA SKIN DE BLOQUEADO ESTÁ SELECIONÁVEL
    c   ADICIONAR OS FAVICONS EM TODAS AS PÁGINAS
    c   CONFIGURAR OS LINKS QUE ESTÃO ERRADOS
    c   TIRAR O TELEFONE DO FORMULÁRIO DE CADASTRO
    c   ADICIONAR AS CONFIGURAÇÕES DA CONTA DO USUÁRIO
    c   MELHORAR O RESPONSSIVO DAS PÁGINAS
    c   ADICIONAR O BUTÃO DE MOSTRAR OU OCULTAR A SENHA
    
    *   ADICIONAR AS FUNÇÕES DA CONFIGURAÇÃO DA CONTA
    *   IMPLEMENTAR O SISTEMA DE ASSINATURA
    *   CONFIGURAR O QUE ESTARÁ DISPONÍVEL EM CADA PLANO
"""