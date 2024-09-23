from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import UserMixin, login_manager
from conexao.conexao import criar_conexao, fexar_conexao

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/formulario')
def formulario():
    return render_template('login.html')

@login_bp.route('/loginValidar', methods=['POST'])
def loginValidar():
    email = request.form.get('email')
    senha = request.form.get('senha')
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = 'select senha from usuarios where email = %s;'
        cursor.execute(sql, email)
        verifiSenha = cursor.fetchall()
        cursor.close()
        fexar_conexao(con)
        if senha == verifiSenha:
            return redirect(url_for('home'))
        else:
            flash('Erro! usuário ou senha inválida.')
            return(redirect(url_for('login.formulario')))
    except:
        flash('Erro! usuário não encontrado.')
        return redirect(url_for('login.formulario'))

@login_bp.route('/logout')
def logout():
    return redirect(url_for('home'))
