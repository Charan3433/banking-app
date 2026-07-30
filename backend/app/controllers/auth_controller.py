from flask import Blueprint, jsonify, request

from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    try:
        user = AuthService.register(data.get("full_name"), data.get("email"), data.get("password"), data.get("phone"), data.get("address"))
        return jsonify({"message": "User registered successfully", "user": user.to_dict()}), 201
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    result = AuthService.login(data.get("email"), data.get("password"))
    if not result:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify(result), 200


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json(silent=True) or {}
    if AuthService.forgot_password(data.get("email")):
        return jsonify({"message": "Password reset instructions sent"}), 200
    return jsonify({"error": "Email not found"}), 404


@auth_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logged out successfully"}), 200
