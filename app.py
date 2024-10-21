from flask import render_template, request, jsonify
from login.login import login_bp
from registrar.registrar import registrar_bp
from plataforma.plataforma import plataforma_bp
from extencoes import criar_app
import stripe
from assinaturas.assinatura import assinatura
from usuario.usuario import usuario


app = criar_app()

stripe.api_key = 'sk_test_51Q83DFB34eoeAWLm0ecXDbomjwhEALJ5FbO8PIXuqjFre8kT0Q2KseMXFZMigilO1NKq0kj3Czv61SoExUww9TMC00Ns8CGOoP'

endpoint_secret = 'whsec_f4924d97d5cc6ae1ceb96cd7ce376900979c058582f36f77dc9b4f53e58a2950'

app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(registrar_bp, url_prefix='/registrar')
app.register_blueprint(plataforma_bp, url_prefix='/plataforma')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    event = None


    try:
        # Verifica a assinatura do webhook para garantir que veio da Stripe
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Falha ao decodificar o payload
        print(f"Erro de valor: {e}")
        return jsonify({'status': 'erro', 'message': 'Payload inválido'}), 400
    except stripe.error.SignatureVerificationError as e:
        # Falha na verificação da assinatura
        print(f"Erro de verificação da assinatura: {e}")
        return jsonify({'status': 'erro', 'message': 'Assinatura inválida'}), 400

    # Agora você pode processar o evento do webhook
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_id = session['customer']
        
        if not session.get('email'):
            customer = stripe.Customer.retrieve(customer_id)
            customer_email = customer['email']
        else:
            customer_email = session.get('email')
        
        print(f"checkout bem sucedido para o cliente com o email: {customer_email}")
        
        assinatura.customer_email = customer_email
        assinatura.customer_id = customer_id
        
        assinatura.atualizarCustomerId(usuario.id_usuario)
    elif event['type'] == 'invoice.payment_succeeded':
        pagamento = event['data']['object']

        if pagamento['total'] == 699:
            print('plano padrão')
            assinatura.atualizarTipoPlano(usuario.id_usuario, 'padrao')
            assinatura.liberarPersonagens(usuario.id_usuario, 'padrao')
        elif pagamento['total'] == 999:
            print('plano proficional')
            assinatura.atualizarTipoPlano(usuario.id_usuario, 'profissional')
            assinatura.liberarPersonagens(usuario.id_usuario, 'profissional')
        
    else:
        print(f"Evento não tratado: {event['type']}")

    return jsonify({'status': 'sucesso'}), 200
    

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