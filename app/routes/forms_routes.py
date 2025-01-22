from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired

# Formulaire d'ajout du tableau
class AddTableauForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    description = TextAreaField('Description')
    prix = FloatField('Prix', validators=[DataRequired()])
    image_path = FileField('Image')
    submit = SubmitField('Ajouter')

# Formulaire de modification du tableau
class EditTableauForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    description = TextAreaField('Description')
    prix = FloatField('Prix', validators=[DataRequired()])
    image_path = FileField('Image')
    submit = SubmitField('Modifier')
