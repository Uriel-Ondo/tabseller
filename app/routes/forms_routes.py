from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, FileField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

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

# Formulaire d'inscription
class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmez le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('S\'inscrire')
