import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.main_routes import main_bp
    from .routes.admin_routes import admin_bp
    from .routes.auth_routes import auth_bp  # Ajoutez cette ligne

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Ajoutez cette ligne

    login_manager.login_view = 'auth.login'

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
