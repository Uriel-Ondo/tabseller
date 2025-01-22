from .. import db
from ..models import Tableau
from .forms_routes import AddTableauForm, EditTableauForm
from flask import current_app, Blueprint, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

from flask_login import login_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@login_required
def admin():
    tableaux = Tableau.query.all()
    return render_template('admin.html', tableaux=tableaux)

@admin_bp.route('/add_tableau', methods=['GET', 'POST'])
@login_required
def add_tableau():
    form = AddTableauForm()
    if form.validate_on_submit():
        filename = None
        if form.image_path.data:
            filename = secure_filename(form.image_path.data.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.image_path.data.save(filepath)

        nouveau_tableau = Tableau(
            nom=form.nom.data,
            description=form.description.data,
            prix=form.prix.data,
            image_path=filename
        )

        db.session.add(nouveau_tableau)
        db.session.commit()

        flash('Le tableau a été ajouté avec succès !', 'success')
        return redirect(url_for('admin.add_tableau'))
    
    return render_template('add_tableau.html', form=form)

@admin_bp.route('/edit_tableau/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_tableau(id):
    tableau = Tableau.query.get_or_404(id)
    form = EditTableauForm(obj=tableau)
    if form.validate_on_submit():
        if form.image_path.data:
            filename = secure_filename(form.image_path.data.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            form.image_path.data.save(filepath)
            tableau.image_path = filename

        tableau.nom = form.nom.data
        tableau.description = form.description.data
        tableau.prix = form.prix.data

        db.session.commit()
        flash('Le tableau a été modifié avec succès !', 'success')
        return redirect(url_for('admin.admin'))

    return render_template('edit_tableau.html', form=form, tableau=tableau)

@admin_bp.route('/delete_tableau/<int:id>', methods=['POST'])
@login_required
def delete_tableau(id):
    tableau = Tableau.query.get_or_404(id)
    db.session.delete(tableau)
    db.session.commit()
    flash('Le tableau a été supprimé avec succès !', 'success')
    return redirect(url_for('admin.admin'))
