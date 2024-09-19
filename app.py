from flask import Flask, render_template
from login.login import login_bp
from registrar.registrar import registrar_bp

app = Flask(__name__)

app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(registrar_bp, url_prefix='/registrar')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
