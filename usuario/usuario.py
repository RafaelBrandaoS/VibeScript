# from flask import redirect, url_for, flash
from conexao.conexao import criar_conexao, fexar_conexao
from flask import url_for
from flask_mail import Message
from extencoes import mail
from datetime import date

dia_atual = date.today()

class Usuario:
    logado = False
    username = ''
    id_usuario = ''
    
    def registrar(self, nome, email, senha, confirm_senha):
        if senha == confirm_senha:
            con = criar_conexao()
            cursor = con.cursor()
            try:
                con.start_transaction()
                
                sql = "insert into usuarios(nome, email, senha) values (%s, %s, %s);"
                values = (nome, email, senha)
                cursor.execute(sql, values)
                
                self.id_usuario = cursor.lastrowid
                self.username = nome
                
                print(self.id_usuario)
                
                sql2 = f"insert into relacaoUsuarioPersonagem (id_usuario, id_personagem, nome_personagem, caracteristicas_personagem) values ('{self.id_usuario}', '10', 'Criar', ''),  ('{self.id_usuario}', '17', 'Bloqueado', ''),  ('{self.id_usuario}', '17', 'Bloqueado', ''), ('{self.id_usuario}', '17', 'Bloqueado', ''),  ('{self.id_usuario}', '17', 'Bloqueado', ''),  ('{self.id_usuario}', '17', 'Bloqueado', '');"
                cursor.execute(sql2)

                
                print(dia_atual)
                
                sql3 = f"insert into inscricoes (id_usuario, plano, plano_status, data_inicio) values ('{self.id_usuario}', 'basico', 'ativo', '{dia_atual}');"
                cursor.execute(sql3)

                con.commit()
                
                return 'ok'
            except:
                return 'erro'
            finally:
                cursor.close()
                fexar_conexao(con)
            
        else:
            return 'erro'
    
    def enviarConfirmacaoEmail(self, userEmail, s):
        
        token = s.dumps(userEmail, salt='email-confirm')
        confirm_url = url_for('registrar.confirm_email', token=token, _external=True)
        
        mensagem = f"""
        <h2>Olá, {self.username}, seja bem vindo ao VibeScript</h2>
        <p>para que sua conta seja ativada confime o seu email clicando no link abaixo</p>
        <a href="{confirm_url}">CONFIRMAR EMAIL</a>
        <br>
        <p>se não foi você que se cadastrou no VibeScript, ignore essa mensagem.</p>
        """
        
        msg = Message('Confirme seu endereço de e-mail', recipients=[userEmail])
        msg.html = mensagem
        mail.send(msg)
    
    def atualizaStatus(self):
        con = criar_conexao()
        cursor =con.cursor()
        sql = f"update usuarios set status_email = 'verificado' where id = '{self.id_usuario}';"
        cursor.execute(sql)
        con.commit()
        cursor.close()
        fexar_conexao(con)
    
    def login(self, email, senha):
        try:
            con = criar_conexao()
            cursor = con.cursor()
            sql = f"select nome, senha, id, status_email from usuarios where email = '{email}';"
            cursor.execute(sql)
            dados = cursor.fetchall()
            print(dados)
            cursor.close()
            fexar_conexao(con)
            if senha == dados[0][1]:
                if dados[0][3] == 'verificado':
                    Usuario.logado = True
                    self.username = dados[0][0]
                    self.id_usuario = dados[0][2]
                    return 'ok'
                else:
                    Usuario.logado = False
                    return 'ERRO! confirme o seu email.'
            else:
                Usuario.logado = False
                return 'ERRO! usuário ou senha inválidos'
        except:
            Usuario.logado = False
            return 'ERRO! não foi possível fazer login.'

    
    def logout(self):
        Usuario.logado = False
        self.username = ''

usuario = Usuario()
