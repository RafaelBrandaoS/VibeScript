from flask import Blueprint, render_template, redirect, url_for
from usuario.usuario import usuario

plataforma_bp = Blueprint('plataforma', __name__, template_folder='templates')

@plataforma_bp.route('/')
def plataformaHome():
    if usuario.logado == True:
        return render_template('plataforma.html', nome=usuario.username)
    else:
        return redirect(url_for('home'))

@plataforma_bp.route('/planos')
def planos():
    return render_template('planos.html')

@plataforma_bp.route('/chat')
def chat():
    return render_template('chat.html')