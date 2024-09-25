# from flask import redirect, url_for, flash
from conexao.conexao import criar_conexao, fexar_conexao


class Usuario:
    logado = False
    username = ''
    id_usuario = ''
    
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
                
                con1 = criar_conexao()
                cursor1 = con1.cursor()
                sql1 = f"select id from usuarios where email = '{email}';"
                cursor1.execute(sql1)
                id_usuario = cursor1.fetchall()
                cursor1.close()
                fexar_conexao(con1)
                
                con2 = criar_conexao()
                cursor2 = con2.cursor()
                sql2 = f"insert into relacaoUsuarioPersonagem (id_usuario, id_personagem, nome_personagem, caracteristicas_personagem) values ('{id_usuario[0][0]}', '10', 'Criar', ''),  ('{id_usuario[0][0]}', '10', 'Criar', ''),  ('{id_usuario[0][0]}', '10', 'Criar', '');"
                cursor2.execute(sql2)
                con2.commit()
                cursor2.close()
                fexar_conexao(con2)
                print(id_usuario)
                
                
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
            sql = f"select nome, senha, id from usuarios where email = '{email}';"
            cursor.execute(sql)
            dados = cursor.fetchall()
            print(dados)
            cursor.close()
            fexar_conexao(con)
            if senha == dados[0][1]:
                Usuario.logado = True
                self.username = dados[0][0]
                self.id_usuario = dados[0][2]
                print(self.id_usuario)
            else:
                Usuario.logado = False
        except:
            Usuario.logado = False
    
    def logout(self):
        Usuario.logado = False
        self.username = ''

usuario = Usuario()
