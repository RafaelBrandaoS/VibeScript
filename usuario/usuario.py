# from flask import redirect, url_for, flash
from conexao.conexao import criar_conexao, fexar_conexao


class Usuario:
    logado = False
    username = ''
    
    def registrar(self, nome, email, telefone, senha, confirm_senha):
        if senha == confirm_senha:
            try:
                con = criar_conexao()
                cursor = con.cursor()
                sql = "insert into usuarios(nome, email, telefone, senha) values (%s, %s, %s, %s);"
                values = (nome, email, telefone, senha)
                cursor.execute(sql, values)
                con.commit()
                cursor.close()
                fexar_conexao(con)
                
                Usuario.logado = True
                
                self.username = nome
                
                return 'ok'
            except:
                Usuario.logado = False
                
                return 'erro'
            
        else:
            Usuario.logado = False
            
            return 'erro'
    
    def login(self, email, senha):
        try:
            con = criar_conexao()
            cursor = con.cursor()
            sql = f"select nome, senha from usuarios where email = '{email}';"
            cursor.execute(sql)
            dados = cursor.fetchall()
            print(dados)
            cursor.close()
            fexar_conexao(con)
            if senha == dados[0][1]:
                Usuario.logado = True
                self.username = dados[0][0]
            else:
                Usuario.logado = False
        except:
            Usuario.logado = False
    
    def logout(self):
        Usuario.logado == False
        self.username = ''

usuario = Usuario()
