from flask import Flask, render_template
from login.login import login_bp

app = Flask(__name__)

app.register_blueprint(login_bp, url_prefix='/login')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
