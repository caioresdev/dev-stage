from flask import Flask, request, jsonify
from src.routes.events import event_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)

