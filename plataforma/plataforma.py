from flask import Blueprint, render_template

plataforma_bp = Blueprint('plataforma', __name__, template_folder='templates')

@plataforma_bp.route('/')
def plataformaHome():
    return render_template('plataforma.html')

@plataforma_bp.route('/planos')
def planos():
    return render_template('planos.html')

@plataforma_bp.route('/chat')
def chat():
    return render_template('chat.html')