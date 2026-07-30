import os

from flask import Flask

from app.config import config_by_name
from app.extensions import cors, db, migrate
from app.logging_config import setup_logging
from app.models import Account, AuditLog, Beneficiary, Transaction, User
from app.routes import register_blueprints


def create_app(config_name=None):
    app = Flask(__name__)
    config_name = config_name or os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})
    setup_logging(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()
        from app.seed import seed_database

        seed_database()

    return app
