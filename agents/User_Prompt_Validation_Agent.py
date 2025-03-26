from typing import Tuple
import autogen
from llm_config import llm_config
from savefile import save_to_file
from agents.User_Proxy_Agent import user_proxy


# Code Review Agent
system_message = """You are a user prompt validator agent.
Your job is to:
1. Analyse the user given prompt/requirement
2. Check the user is talking about creating or developing a code/Application, then consider it as valid prompt
3. If the prompt is not related to creating a application or generating a code, then consider it as invalid prompt
Be thorough but fair. Cite specific issues and suggest users to provide a valid prompt.
"""

validator_agent = autogen.AssistantAgent(
    name="UserPromptValidator",
    system_message=system_message,
    llm_config=llm_config
)

def validate_prompt(state) -> Tuple[bool, str]:

        requirements = state["Requirement"]
        user_proxy.initiate_chat(
            validator_agent,
            message=f"""Please analyse the following user given prompt and check whether given prompt is valid or not.
            \n
            PROMPT:
            {requirements}
            
            Please provide detailed feedback and explicitly state if the prompt is Valid 
            or Invalid. If it is invalid, clearly explain what is valid prompt.
            """
        )
        
        # Extract the review from the conversation
        last_message = validator_agent.last_message()
        analysis_report = last_message["content"]
        
        # Determine if the code passed review
        valid = "VALID" in analysis_report.upper() and "INVALID" not in analysis_report.upper()
        
        return valid,analysis_report
    