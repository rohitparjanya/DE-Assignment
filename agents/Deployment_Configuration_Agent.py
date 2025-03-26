from typing import Tuple
import autogen
from llm_config import llm_config
from savefile import save_to_file
from agents.User_Proxy_Agent import user_proxy


# Code Review Agent
system_message = """You are a senior DevOps engineer.
1.Based on the provided requirements and codebase, create a deployment configuration.
2.Ensure the configuration achieves scalability, security, and efficiency.
Include the following:
Recommended deployment strategies.\n
CI/CD pipeline setup and tools.\n
Infrastructure as Code (IaC) configurations.\n
Monitoring and logging practices.\n
Provide clear, actionable steps in your response.
"""
deployment_config_agent = autogen.AssistantAgent(
    name="DeploymentConfigurator",
    system_message=system_message,
    llm_config=llm_config
)

def run_deployment_config_generator( state) -> Tuple[bool, str]:
        requirements = state["Requirement"]
        code = state["Code"]
        user_proxy.initiate_chat(
            deployment_config_agent,
            message=f"""The following are the requirements and code of a application.You should provide the deployment config file suitable for the given requirement and code..
            
            REQUIREMENTS:
            {requirements}
            
            CODE:
            ```python
            {code}
            ```
            \n\n
            
            """
        )
        # Extract the review from the conversation
        last_message = deployment_config_agent.last_message()
        deployement_config_content = last_message["content"]
        state["Deployment Configuration"] = deployement_config_content
        # Save to file
        save_to_file(deployement_config_content, "output/deployement_config_file.py")
        
        return deployement_config_content,5