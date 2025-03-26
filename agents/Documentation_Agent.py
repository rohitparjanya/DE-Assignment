from typing import Tuple
import autogen
from llm_config import llm_config
from savefile import save_to_file
from agents.User_Proxy_Agent import user_proxy

# Documentation Agent
system_message = """You are a documentation specialist.
Your job is to:
1. Create comprehensive documentation for Python code
2. Follow standard documentation formats
3. Include overview, installation instructions, usage examples, and API references
4. Ensure documentation is clear for both technical and non-technical users
5. Use Markdown format for the documentation

Focus on clarity, completeness, and usability.
"""
doc_agent = autogen.AssistantAgent(
    name="DocumentationSpecialist",
    system_message=system_message,
    llm_config=llm_config
)
def run_documentation_generation(state) -> str:
        requirements = state["Requirement"]
        code = state["Code"]
        user_proxy.initiate_chat(
            doc_agent,
            message=f"""Please generate comprehensive documentation for the following Python code.
            Include project overview, installation instructions, usage examples, and API reference.
            
            REQUIREMENTS:
            {requirements}
            
            CODE:
            ```python
            {code}
            ```
            
            Please provide well-structured Markdown documentation that would help users understand and use this code.
            """
        )
        
        # Extract the documentation from the conversation
        last_message = doc_agent.last_message()
        documentation = last_message["content"]
        state["Documentation"] = documentation
        
        
        # Save to file
        save_to_file(documentation, "output/docs/readme.md")
        
        return documentation,3
    