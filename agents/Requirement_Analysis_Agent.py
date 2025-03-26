# Requirement Analysis Agent
from typing import Tuple
import autogen
from llm_config import llm_config
from savefile import save_to_file

from agents.User_Proxy_Agent import user_proxy
system_message = """You are a requirement analysis expert. 
Your job is to:
1. Take natural language requirements
2. Structure them into clear, detailed software requirements
3. Identify any ambiguities or missing details and resolve them
4. Organize requirements into functional, non-functional, and technical categories
5. Output a JSON format with the structured requirements

Your response should be clear, thorough, and actionable for the coding team.
"""
req_analysis_agent = autogen.AssistantAgent(
    name="RequirementAnalyst",
    system_message=system_message,
    llm_config=llm_config
)

def run_requirement_analysis(state) -> str:
        user_given_prompt = state.get("Requirement")
        # Start a conversation with the requirement analysis agent
        user_proxy.initiate_chat(
            req_analysis_agent,
            message=f"""Please analyze and structure the following requirements into a detailed, 
            JSON-formatted software specification. Identify all functional and non-functional requirements.
            
            REQUIREMENTS:
            {user_given_prompt}
            
            Output the structured requirements in JSON format with appropriate sections for:
            - Project overview
            - Functional requirements (broken down by feature/component)
            - Non-functional requirements
            - Technical constraints
            - API specifications (if applicable)
            - Data models (if applicable)
            """
        )
        
        # Extract the structured requirements from the conversation
        last_message = req_analysis_agent.last_message()
        state["Requirement Analysis"] = last_message["content"]
        
        # Save to file
        save_to_file(state["Requirement Analysis"], "output/Requirement_Analysis.json")
        
        return state["Requirement Analysis"],0
    