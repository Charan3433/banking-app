from flask import Blueprint, jsonify, request

from app.models.account import Account
from app.models.transaction import Transaction
from app.repositories.user_repository import UserRepository
from app.utils.auth_utils import token_required

user_bp = Blueprint("user", __name__)


@user_bp.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return jsonify({"user": current_user.to_dict()}), 200


@user_bp.route("/dashboard", methods=["GET"])
@token_required
def dashboard(current_user):
    accounts = Account.query.filter_by(user_id=current_user.id).all()
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.created_at.desc()).limit(5).all()
    total_balance = sum(float(account.balance) for account in accounts)
    return jsonify({
        "user": current_user.to_dict(),
        "total_balance": round(total_balance, 2),
        "account_count": len(accounts),
        "recent_transactions": [transaction.to_dict() for transaction in transactions],
    }), 200


@user_bp.route("/profile", methods=["PUT"])
@token_required
def update_profile(current_user):
    data = request.get_json(silent=True) or {}
    current_user.full_name = data.get("full_name", current_user.full_name)
    current_user.phone = data.get("phone", current_user.phone)
    current_user.address = data.get("address", current_user.address)
    UserRepository.update(current_user)
    return jsonify({"message": "Profile updated", "user": current_user.to_dict()}), 200
