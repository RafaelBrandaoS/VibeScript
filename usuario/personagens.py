from conexao.conexao import criar_conexao, fexar_conexao
from usuario.usuario import usuario

class Personagem:
    nome = ''
    aparencia = ''
    caracteristicas = ''
    
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

personagens = Personagem()
