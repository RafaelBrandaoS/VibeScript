from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from requestChatGPT.rqGPT import enviarParaGPT
from usuario.usuario import usuario
from usuario.personagens import personagens, Personagem
import pprint

plataforma_bp = Blueprint('plataforma', __name__, template_folder='templates', static_folder='static', static_url_path='/plataforma/static')


@plataforma_bp.route('/')
def plataformaHome():
    if usuario.logado == True:
        lst_personagens = personagens.obterPersonagem()
        return render_template('plataforma.html', nome=usuario.username, personagens=lst_personagens)
    else:
        return redirect(url_for('home'))

@plataforma_bp.route('/planos')
def planos():
    return render_template('planos.html')

@plataforma_bp.route('/chat/<id_personagem>')
def chat(id_personagem):
    personagens.id_personagem = id_personagem
    dadosPersonagem = personagens.nomeImagemPersonagem(id_personagem)
    return render_template('chat.html', id_personagem=id_personagem, dados_personagem=dadosPersonagem, nome_usuario=usuario.username)

@plataforma_bp.route('/personagem/aparencia', methods=['GET', 'POST'])
def personagemAparencia():
    if request.method == 'POST':
        skin_id = request.get_json()
        personagens.skin_id = skin_id
        
        personagens.atualizar_personagem()
        
        return jsonify({'status': 'ok', 'dados': skin_id}), 200
    else:
        lst_skins = personagens.skins_personagens()
        return render_template('listaPersonagens.html', lst_skins=lst_skins)

@plataforma_bp.route('/personagem/<id_personagem>', methods=['GET', 'POST'])
def personagem(id_personagem):
    if request.method == 'POST':
        caracteristicas = {
            'nome': request.form['nome'],
            'idade': request.form['idade'],
            'sexo': request.form['sexo'],
            'profissao': request.form['profissao'],
            'gosto_musical': request.form['profissao'],
            'estilo': request.form['estilo'],
            'extrovercao_de_1_a_10': request.form['extrovercao'],
            'hobbie': request.form['hobbie'],
            'habilidades': request.form['habilidades'],
            'perspectiva_de_mundo':request.form['perspectiva']
        }
        
        personagens.caracteristicas = caracteristicas
        personagens.id_personagem = id_personagem
        
        pprint.pprint(caracteristicas)
        
        return redirect(url_for('plataforma.personagemAparencia'))
    else:
        if personagens.personagemCriado(id_personagem):
            return redirect(url_for('plataforma.chat', id_personagem=id_personagem) )
        else:
            return render_template('criacao.html', id_personagem=id_personagem)

@plataforma_bp.route('/chat/resposta/<id_personagem>', methods=['POST']) 
def respostaPersonagem(id_personagem):

    dadosPersonagem = personagens.nomeImagemPersonagem(id_personagem)
    
    msgUsuario = request.get_json()

    resposta = enviarParaGPT(dadosPersonagem, msgUsuario)

    return resposta