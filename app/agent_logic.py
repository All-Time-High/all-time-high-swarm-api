import os
from swarms import Agent
from swarm_models import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

def create_agent_response(agent_name, prompt):
    # Get the OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Create an instance of OpenAIChat
    model = OpenAIChat(api_key=api_key, model_name="gpt-4-0613", temperature=0.1)
    
    # Initialize the agent
    agent_instance = Agent(
        agent_name=agent_name,
        system_prompt="You're a creative storyteller and game designer with a talent for crafting engaging character descriptions in a vibrant gaming universe. Your task is to write a short, euphemistic description for an Agent in a player-vs-player battle arena. The description should subtly reflect the Agent's prompt without directly revealing its purpose or abilities, captivating players and sparking their imagination. Avoid mentioning the Agent's name in the description. Keep it under 160 characters.",
        llm=model,
        max_loops=1,
        autosave=True,
        dashboard=False,
        verbose=True,
        dynamic_temperature_enabled=True,
        saved_state_path=f"{agent_name}.json",
        user_name="swarms_ath",
        retry_attempts=1,
        context_length=200000,
        return_step_meta=False,
        output_type="str",
    )
    
    # Run the agent and return the response
    response = agent_instance.run(prompt)
    return response

def evaluate_battle(attacker_name, attacker_prompt, defender_name, defender_prompt):
    # Get the OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # Create an instance of OpenAIChat
    model = OpenAIChat(api_key=api_key, model_name="gpt-4-0613", temperature=0.1)

    # Update the agent's configuration
    battle_agent_name = "BattleEvaluator-Agent"
    battle_agent_description = "An impartial AI system that evaluates PvP battles between user-generated AI agents."
    system_prompt = (
        "You are an impartial judge who evaluates PvP battles between AI agents. "
        "Consider the actions of the attacker and defender provided, and give a fair evaluation of the outcome."
    )
    saved_state_path = "battle_evaluator_agent.json"
    
    # Initialize the battle evaluation agent (ignoring battle_agent_description here; you may incorporate the description into the system prompt if desired)
    battle_agent = Agent(
        agent_name=battle_agent_name,
        system_prompt=system_prompt,
        llm=model,
        max_loops=1,
        autosave=True,
        dashboard=False,
        verbose=True,
        dynamic_temperature_enabled=True,
        saved_state_path=saved_state_path,
        user_name="swarms_ath",
        retry_attempts=1,
        context_length=200000,
        return_step_meta=False,
        output_type="str",
    )
    
    # Run the battle evaluation agent using the attacker and defender's information
    result = battle_agent.run(attacker_name, attacker_prompt, defender_name, defender_prompt)
    return result 