from conexao.conexao import criar_conexao, fexar_conexao
from flask import jsonify
# from flask_mail import Message
# from extencoes import mail
# from datetime import date

# dia_atual = date.today()

class Assinatura:
    customer_id = None
    customer_email = None
    
    def atualizarCustomerId(self, id_usuario):
        try:
            con = criar_conexao()
            cursor = con.cursor()
            con.start_transaction()
            sql = f"update inscricoes set customer_id = '{self.customer_id}' where id_usuario = '{id_usuario}';"
            cursor.execute(sql)
            con.commit()
            cursor.close()
            fexar_conexao(con)
        except ValueError as e:
            print(f'ERRO: {e}')
            return jsonify({'status': 'erro', 'message': 'erro ao cadastrar o customer_id'}), 400
        
        return jsonify({'status': 'sucesso'}), 200
    
    def atualizarTipoPlano(self, id_usuario, tipo_plano):
        try:
            con = criar_conexao()
            cursor = con.cursor()
            sql = f"update  inscricoes set plano = '{tipo_plano}' where id_usuario = '{id_usuario}';"
            cursor.execute(sql)
            con.commit()
            cursor.close()
            fexar_conexao(con)
        except ValueError as e:
            print(f'erro: {e}')
            return jsonify({'status': 'erro', 'message': 'erro ao atualizar o plano'}), 400

        return jsonify({'status': 'secesso'}), 200
    
    def liberarPersonagens(self, id_usuario, tipo_plano):
        try:
            con = criar_conexao()
            cursor = con.cursor()
            sql = f"select * from relacaoUsuarioPersonagem where id_usuario = '{id_usuario}';"
            cursor.execute(sql)
            dados = cursor.fetchall()
            cursor.close()
            fexar_conexao(con)
            
        except ValueError as e:
            print(f'erro: {e}')
            return jsonify({'status': 'erro', 'message': 'erro ao obter os dados do personagem'}), 400
        
        def atualizarListaPersonagens(id_personagem):
            con = criar_conexao()
            cursor = con.cursor()
            sql = f"update relacaoUsuarioPersonagem set nome_personagem = 'Criar', id_personagem = '10' where id = {id_personagem};"
            cursor.execute(sql)
            con.commit()
            cursor.close()
            fexar_conexao(con)
        
        for i, personagem in enumerate(dados):
            if tipo_plano == 'padrao':
                if i == 1 or i == 2:
                    atualizarListaPersonagens(personagem[0])
            elif tipo_plano == 'profissional':
                if i >= 1:
                    atualizarListaPersonagens(personagem[0])
            
        
        return jsonify({'status': 'sucesso'}), 200

assinatura = Assinatura()
