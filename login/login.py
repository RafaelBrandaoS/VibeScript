from flask import Blueprint, render_template, redirect, url_for, request, flash
# from flask_login import UserMixin, login_manager
from usuario.usuario import usuario

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/formulario')
def formulario():
    return render_template('login.html')

@login_bp.route('/loginValidar', methods=['POST'])
def loginValidar():
    email = request.form.get('email')
    senha = request.form.get('senha')
    status_login = usuario.login(email, senha)
    if status_login == 'ok':
        return redirect(url_for('plataforma.plataformaHome'))
    else: 
        flash(status_login)
        return(redirect(url_for('login.formulario')))
    

@login_bp.route('/logout')
def logout():
    usuario.logout()
    return redirect(url_for('home'))
