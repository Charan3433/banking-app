from app.controllers.account_controller import account_bp
from app.controllers.auth_controller import auth_bp
from app.controllers.health_controller import health_bp
from app.controllers.user_controller import user_bp
from app.controllers.transaction_controller import transaction_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(account_bp, url_prefix="/api/accounts")
    app.register_blueprint(transaction_bp, url_prefix="/api/transactions")
    app.register_blueprint(health_bp, url_prefix="/api/health")
