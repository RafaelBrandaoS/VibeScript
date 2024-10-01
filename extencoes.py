from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os 

load_dotenv()
SENHA_EMAIL = os.getenv('SENHA_EMAIL')

chaveSecreta = os.urandom(24)

mail = Mail()

def criar_app():
    app = Flask(__name__)

    app.secret_key = chaveSecreta
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'vibescript.com@gmail.com'
    app.config['MAIL_PASSWORD'] = SENHA_EMAIL
    app.config['MAIL_DEFAULT_SENDER'] = 'vibescript.com@gmail.com'

    mail.init_app(app)
    
    return app
