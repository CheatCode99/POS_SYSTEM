from flask import Blueprint, jsonify

error_bp = Blueprint('error', __name__)

@error_bp.app_errorhandler(404)
def error_404(e):
    return jsonify({
        "status": 404,
        "message": "Page Not Found"
    }), 404