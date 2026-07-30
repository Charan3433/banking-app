from flask import Blueprint, jsonify, request

from app.models.account import Account
from app.models.transaction import Transaction
from app.repositories.account_repository import AccountRepository
from app.services.account_service import AccountService
from app.utils.auth_utils import token_required

transaction_bp = Blueprint("transaction", __name__)


@transaction_bp.route("", methods=["GET"])
@token_required
def history(current_user):
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.created_at.desc()).all()
    return jsonify({"transactions": [tx.to_dict() for tx in transactions]}), 200


@transaction_bp.route("/deposit", methods=["POST"])
@token_required
def deposit(current_user):
    data = request.get_json(silent=True) or {}
    try:
        account = AccountService.deposit(data.get("account_id"), float(data.get("amount", 0)), current_user.id)
        return jsonify({"message": "Deposit successful", "account": account.to_dict()}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@transaction_bp.route("/withdraw", methods=["POST"])
@token_required
def withdraw(current_user):
    data = request.get_json(silent=True) or {}
    try:
        account = AccountService.withdraw(data.get("account_id"), float(data.get("amount", 0)), current_user.id)
        return jsonify({"message": "Withdrawal successful", "account": account.to_dict()}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@transaction_bp.route("/transfer", methods=["POST"])
@token_required
def transfer(current_user):
    data = request.get_json(silent=True) or {}
    try:
        account = AccountService.transfer(int(data.get("from_account_id")), data.get("to_account_number"), float(data.get("amount", 0)), current_user.id)
        return jsonify({"message": "Transfer successful", "account": account.to_dict()}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
