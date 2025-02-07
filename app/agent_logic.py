import os
from swarms import Agent
from swarm_models import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

def create_agent_response(agent_name, prompt):
    # 从环境变量中获取 OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    # 创建 OpenAIChat 实例
    model = OpenAIChat(api_key=api_key, model_name="gpt-4-0613", temperature=0.1)
    
    # 初始化 agent
    agent_instance = Agent(
        agent_name=agent_name,
        system_prompt="You're a creative storyteller and game designer with a talent for crafting engaging character descriptions in a vibrant gaming universe. Your task is to write a short, euphemistic description for an Agent in a player-vs-player battle arena. The description should subtly reflect the Agent's prompt without directly revealing its purpose or abilities, captivating players and sparking their imagination. Avoid mentioning the Agent's name in the description. Keep it under 160 characters.",
        llm=model,
        max_loops=1,
        autosave=True,
        dashboard=False,
        verbose=True,
        dynamic_temperature_enabled=True,
        saved_state_path="battle_agent.json",
        user_name="swarms_corp",
        retry_attempts=1,
        context_length=200000,
        return_step_meta=False,
        output_type="str",
    )
    
    # 运行 agent，并返回响应
    response = agent_instance.run(prompt)
    return response 