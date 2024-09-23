from flask import Blueprint, render_template, request, redirect, url_for, flash
from conexao.conexao import criar_conexao, fexar_conexao

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
    
    if senha == confirm_senha:
        try:
            con = criar_conexao()
            cursor = con.cursor()
            sql = "insert into usuarios(nome, email, telefone, senha) values (%s, %s, %s, %s);"
            values =(nome, email, telefone, senha)
            cursor.execute(sql, values)
            con.commit()
            cursor.close()
            fexar_conexao(con)
            
            return redirect(url_for('plataforma.plataforma'))
        except:
            flash('Erro! erro ao criar a conta.')
            return redirect(url_for('registrar.formulario'))
        
    else:
        flash('Erro! as senhas devem ser iguais.')
        return redirect(url_for('registrar.formulario'))
    