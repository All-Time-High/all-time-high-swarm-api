from flask import Blueprint, jsonify, request
from app.agent_logic import create_agent_response, evaluate_battle

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

@api_bp.route('/evaluateBattle', methods=['GET'])
def evaluate_battle_route():
    attacker_name = request.args.get('attacker_name')
    attacker_prompt = request.args.get('attacker_prompt')
    defender_name = request.args.get('defender_name')
    defender_prompt = request.args.get('defender_prompt')
    result = evaluate_battle(attacker_name, attacker_prompt, defender_name, defender_prompt)
    return jsonify({"result": result}) 