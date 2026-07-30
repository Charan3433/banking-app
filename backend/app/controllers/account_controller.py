from flask import Blueprint, jsonify, request

from app.repositories.account_repository import AccountRepository
from app.services.account_service import AccountService
from app.utils.auth_utils import token_required

account_bp = Blueprint("account", __name__)


@account_bp.route("", methods=["POST"])
@token_required
def create_account(current_user):
    data = request.get_json(silent=True) or {}
    account = AccountService.create_account(current_user.id, data.get("account_type", "checking"))
    return jsonify({"message": "Account created", "account": account.to_dict()}), 201


@account_bp.route("", methods=["GET"])
@token_required
def list_accounts(current_user):
    accounts = AccountRepository.get_user_accounts(current_user.id)
    return jsonify({"accounts": [account.to_dict() for account in accounts]}), 200


@account_bp.route("/<int:account_id>", methods=["GET"])
@token_required
def account_details(current_user, account_id):
    account = AccountRepository.get_by_id(account_id)
    if not account or account.user_id != current_user.id:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({"account": account.to_dict()}), 200
