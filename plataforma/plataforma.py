from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from requestChatGPT.rqGPT import enviarParaGPT
from usuario.usuario import usuario
from usuario.personagens import personagens, Personagem
import pprint

plataforma_bp = Blueprint('plataforma', __name__, template_folder='templates', static_folder='static', static_url_path='/plataforma/static')



@plataforma_bp.route('/')
def plataformaHome():
    if usuario.logado:
        lst_personagens = personagens.obterPersonagem()
        return render_template('plataforma.html', nome=usuario.username, personagens=lst_personagens)
    else:
        return redirect(url_for('home'))

@plataforma_bp.route('/planos')
def planos():
    if usuario.logado:
        infos_plano = usuario.planoUsuario()
        return render_template('planos.html', infos_plano=infos_plano)
    else:
        return redirect(url_for('home'))

@plataforma_bp.route('/chat/<id_personagem>')
def chat(id_personagem):
    if usuario.logado:
        personagens.id_personagem = id_personagem
        dadosPersonagem = personagens.nomeImagemPersonagem(id_personagem)
        print(dadosPersonagem)
        if dadosPersonagem['id_skin'] == 10 or dadosPersonagem['id_skin'] == 17 or dadosPersonagem['id_usuario'] != usuario.id_usuario:
            return redirect(url_for('plataforma.plataformaHome'))
        else:
            return render_template('chat.html', id_personagem=id_personagem, dados_personagem=dadosPersonagem, nome_usuario=usuario.username)
    else:
        return redirect(url_for('home'))

@plataforma_bp.route('/personagem/aparencia', methods=['GET', 'POST'])
def personagemAparencia():
    if request.method == 'POST':
        skin_id = request.get_json()
        personagens.skin_id = skin_id
        
        personagens.atualizar_personagem()
        
        return jsonify({'status': 'ok', 'dados': skin_id}), 200
    else:
        if usuario.logado:
            if personagens.caracteristicas != {}:
                lst_skins = personagens.skins_personagens()
                return render_template('listaPersonagens.html', lst_skins=lst_skins)
            else:
                return redirect(url_for('plataforma.plataformaHome'))
        else:
            return redirect(url_for('home'))

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
        if usuario.logado:
            st_personagem = personagens.statusPersonagem(id_personagem)
            if st_personagem == 'Criar':
                return render_template('criacao.html', id_personagem=id_personagem)
            elif st_personagem == 'Bloqueado':
                flash('Atualize seu plano para ter acesso a mais personagens!')
                return redirect(url_for('plataforma.plataformaHome'))
            else:
                return redirect(url_for('plataforma.chat', id_personagem=id_personagem) )
        else:
            return redirect(url_for('home'))

@plataforma_bp.route('/chat/resposta/<id_personagem>', methods=['POST']) 
def respostaPersonagem(id_personagem):

    dadosPersonagem = personagens.nomeImagemPersonagem(id_personagem)
    
    msgUsuario = request.get_json()

    resposta = enviarParaGPT(dadosPersonagem, msgUsuario)

    return resposta