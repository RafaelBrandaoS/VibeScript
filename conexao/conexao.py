from mysql.connector import connect
from dotenv import load_dotenv
import os


load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')

def criar_conexao():
    return connect(host=DB_HOST, password=DB_PASSWORD, user=DB_USER, port=DB_PORT, database=DB_DATABASE)

def fexar_conexao(con):
    return con.close()