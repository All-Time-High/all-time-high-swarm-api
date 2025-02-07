from flask import Blueprint, jsonify, request
from app.agent_logic import create_agent_response

api_bp = Blueprint('api', __name__)

@api_bp.route('/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({"status": "ok"})

@api_bp.route('/createAgent', methods=['GET'])
def create_agent():
    agent_name = request.args.get('agent_name')
    prompt = request.args.get('prompt')
    response = create_agent_response(agent_name, prompt)
    return jsonify({"response": response}) 