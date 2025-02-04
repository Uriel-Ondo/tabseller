from flask import Blueprint, render_template
from app.models import Tableau

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Récupérer tous les tableaux de la base de données
    tableaux = Tableau.query.all()
    return render_template('index.html', tableaux=tableaux)

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
