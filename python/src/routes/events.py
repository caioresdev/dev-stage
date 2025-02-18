from flask import Blueprint, request, jsonify

event_route_bp = Blueprint('event route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def create_new_event():
    return jsonify(["Salve salve"]), 201

@event_route_bp.route('/events', methods=['GET'])
def verify_event():
    return jsonify({"status": "Online"}), 200