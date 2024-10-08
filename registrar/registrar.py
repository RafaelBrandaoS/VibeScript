from flask import Blueprint, render_template, request, redirect, url_for, flash
from usuario.usuario import usuario
from itsdangerous import URLSafeTimedSerializer
from extencoes import chaveSecreta

registrar_bp = Blueprint('registrar', __name__, template_folder='templates')


s = URLSafeTimedSerializer(chaveSecreta)


@registrar_bp.route('/formulario')
def formulario():
    return render_template('registrar.html')

@registrar_bp.route('/regis_validar', methods=['POST'])
def regis_validar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirm_senha = request.form.get('confirm-senha')
    
    cadastrar = usuario.registrar(nome, email, senha, confirm_senha)
    
    print(cadastrar)
    
    if cadastrar == 'ok':
        usuario.enviarConfirmacaoEmail(email, s)
        flash('Um e-mail de verificação foi enviado para o seu endereço. Verifique sua caixa de entrada.', 'info')
        return redirect(url_for('login.formulario'))
    else:
        flash('Algo deu errado, tente novamente.', 'alert')
        return redirect(url_for('registrar.formulario'))


@registrar_bp.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)  # Verifica o token em até 1 hora
    except:
        flash('O link de confirmação é inválido ou expirou.', 'danger')
        return redirect(url_for('login.login'))
    
    # Aqui você atualizaria o status do usuário para "verificado"
    usuario.atualizaStatus()
    
    flash('E-mail verificado com sucesso!', 'success')
    return redirect(url_for('login.formulario'))