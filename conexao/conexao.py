from mysql.connector import connect
from dotenv import load_dotenv
import os


load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')

def criar_conexao():
    return connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)

def fexar_conexao(con):
    return con.close()