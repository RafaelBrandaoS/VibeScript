from conexao.conexao import criar_conexao, fexar_conexao
from usuario.usuario import usuario

class Personagem:
    caracteristicas = {}
    skin_id = None
    id_personagem = None
    
    def obterPersonagem(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = f"select * from relacaoUsuarioPersonagem where id_usuario = '{usuario.id_usuario}';"

        cursor.execute(sql)
        relacio = cursor.fetchall()
        cursor.close()
        fexar_conexao(con)
        
        skins = []
        relacionamento_formatado = []
        
        
        for p in relacio:
            con1 = criar_conexao()
            cursor1 = con1.cursor()
            sql1 = f"select * from personagens where id = '{p[2]}';"
            cursor1.execute(sql1)
            perso = cursor1.fetchall()
            cursor1.close()
            fexar_conexao(con1)
            
            skin = {'id': perso[0][0], 'nome': perso[0][1], 'caminho_imagem': perso[0][2]}
            
            skins.append(skin)
        
        
        for dado in relacio:
            relacionamento = {'id': dado[0], 'id_usuario': dado[1], 'id_personagem': dado[2], 'nome_personagem': dado[3], 'caracteristicas': dado[4]}
            relacionamento_formatado.append(relacionamento)
            
        
        dados = [relacionamento_formatado, skins]

        
        return dados
    
    def skins_personagens(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "select * from personagens;"
        cursor.execute(sql)
        skins = cursor.fetchall()
        cursor.close()
        fexar_conexao(con)
        
        return skins
    
    def atualizar_personagem(self):
        con = criar_conexao()
        cursor = con.cursor()
        sql = "update relacaoUsuarioPersonagem set id_personagem = %s, nome_personagem = %s, caracteristicas_personagem = %s where id = %s;"
        valores = (self.skin_id, self.caracteristicas['nome'], str(self.caracteristicas), self.id_personagem)
        cursor.execute(sql, valores)
        con.commit()
        cursor.close()
        fexar_conexao(con)
        
        
        print('\n\n')
        print(self.caracteristicas['nome'])
        print('\n\n')
        print(str(self.caracteristicas))
        print('\n\n')
        print(self.skin_id)
        print('\n\n')
        print(self.id_personagem)
        print('\n\n')
    
    def personagemCriado(self, id_personagem):
        con = criar_conexao()
        cursor = con.cursor()
        sql = f"select nome_personagem from relacaoUsuarioPersonagem where id = {id_personagem}"
        cursor.execute(sql)
        nome = cursor.fetchall()
        cursor.close()
        fexar_conexao(con)
        
        print(nome)
        
        if nome[0][0] != 'Criar':
            return True
        else:
            return False
    

personagens = Personagem()
