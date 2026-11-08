from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app(config_name="default"):
    app = Flask(__name__, template_folder="presentation/templates", static_folder="presentation/static")
    if config_name == "test":
        from config import TestConfig
        app.config.from_object(TestConfig)
    else:
        from config import Config
        app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.presentation.auth_routes import auth_bp
    from app.presentation.request_routes import request_bp
    from app.presentation.volunteer_routes import volunteer_bp
    from app.presentation.admin_routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(volunteer_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()
        from app.data.seed import seed_if_empty
        seed_if_empty()

    @login_manager.user_loader
    def load_user(user_id):
        from app.data.repositories import UserRepo
        return UserRepo.get_by_id(int(user_id))

    return app
