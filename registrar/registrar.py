from flask import Blueprint, render_template, request, redirect, url_for, flash
# from conexao.conexao import criar_conexao, fexar_conexao
from usuario.usuario import usuario

registrar_bp = Blueprint('registrar', __name__, template_folder='templates')

@registrar_bp.route('/formulario')
def formulario():
    return render_template('registrar.html')

@registrar_bp.route('/regis_validar', methods=['POST'])
def regis_validar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    senha = request.form.get('senha')
    confirm_senha = request.form.get('confirm-senha')
    
    usuario.registrar(nome, email, telefone, senha, confirm_senha)
    
    if usuario.logado:
        return redirect(url_for('plataforma.plataformaHome'))
    else:
        flash('ERRO! dados inválidos.')
        return redirect('registrar.formulario')
    