from flask import Flask, render_template
import os
from login.login import login_bp
from registrar.registrar import registrar_bp
from plataforma.plataforma import plataforma_bp
from usuario.usuario import Usuario

app = Flask(__name__)
app.secret_key = os.urandom(24)

usuario = Usuario()

app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(registrar_bp, url_prefix='/registrar')
app.register_blueprint(plataforma_bp, url_prefix='/plataforma')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
