from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/formulario')
def formulario():
    return render_template('login.html')
