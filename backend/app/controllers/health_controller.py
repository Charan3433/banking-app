from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "banking-api"}), 200


@health_bp.route("/metrics", methods=["GET"])
def metrics():
    return jsonify({"status": "ok", "metrics": {"requests": 0}}), 200


@health_bp.route("/health", methods=["GET"])
def health_alias():
    return health()
