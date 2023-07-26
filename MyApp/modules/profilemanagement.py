#francisco
from flask import Blueprint, jsonify

bp = Blueprint('profile-management', __name__, url_prefix='/profile-management')

@bp.route('/endpoint1')
def endpoint1():
    return jsonify({"message": "This is Brandon's endpoint!"})
