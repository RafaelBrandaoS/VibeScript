from flask import Blueprint, render_template

plataforma_bp = Blueprint('plataforma', __name__, template_folder='templates')

@plataforma_bp.route('/')
def plataformaHome():
    return render_template('plataforma.html')
