from flask import Blueprint, render_template

registrar_bp = Blueprint('registrar', __name__, template_folder='templates')

@registrar_bp.route('/formulario')
def formulario():
    return render_template('registrar.html')
