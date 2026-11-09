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
    from app.presentation.arch_routes import arch_bp
    from app.presentation.learn_routes import learn_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(volunteer_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(arch_bp)
    app.register_blueprint(learn_bp)

    with app.app_context():
        db.create_all()
        from app.data.seed import seed_if_empty
        seed_if_empty()

    @login_manager.user_loader
    def load_user(user_id):
        from app.data.repositories import UserRepo
        return UserRepo.get_by_id(int(user_id))

    @app.context_processor
    def inject_globals():
        from flask_login import current_user
        unread = 0
        if current_user.is_authenticated:
            from app.data.repositories import NotificationRepo
            unread = NotificationRepo.unread_count(current_user.id)
        return {"unread": unread}

    @app.template_filter("status_label")
    def status_label(s):
        return s.replace("_", " ").title() if s else ""

    @app.template_filter("friendly_time")
    def friendly_time(dt):
        return dt.strftime("%b %d, %Y · %I:%M %p") if dt else ""

    return app
