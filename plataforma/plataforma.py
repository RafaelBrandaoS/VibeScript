from flask import Blueprint, render_template, redirect, url_for
from usuario.usuario import usuario
from usuario.personagens import personagens

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
    return render_template('chat.html', id_personagem=id_personagem)

@plataforma_bp.route('/teste/')
def teste():
    personagens.obterPersonagem()
    return redirect(url_for('plataforma.plataformaHome'))