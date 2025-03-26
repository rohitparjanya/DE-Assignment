from typing import Tuple
import autogen
from llm_config import llm_config
from savefile import save_to_file
from agents.User_Proxy_Agent import user_proxy

system_message = """You are an expert Python developer.
Your job is to:
1. Take structured requirements
2. Develop clean, efficient, and modular Python code that satisfies all requirements
3. Use best practices and design patterns
4. Provide explanatory comments
5. Handle edge cases and errors appropriately

If your code is sent back for revision, carefully analyze the feedback and improve accordingly.
"""
coding_agent = autogen.AssistantAgent(
    name="CodeDeveloper",
    system_message=system_message,
    llm_config=llm_config
)
def run_code_development( state) -> str:
        """Run the coding agent to develop code based on structured requirements."""
       
        user_given_prompt = state.get("Requirement")
        # Start a conversation with the coding agent
        user_proxy.initiate_chat(
            coding_agent,
            message=f"""Please develop Python code according to these structured requirements. 
            Write clean, well-commented, modular code that implements all required functionality.
            
            STRUCTURED REQUIREMENTS:
            {user_given_prompt}
            
            Please provide fully functional Python code that meets all requirements.
            """
        )
        
        # Extract the code from the conversation
        last_message = coding_agent.last_message()
        state["Code"] = last_message["content"]
        
        # Clean up code (extract from markdown if needed)
        if "```python" in state["Code"]:
            code_parts = state["Code"].split("```python")
            for part in code_parts[1:]:
                if "```" in part:
                    clean_code = part.split("```")[0].strip()
                    state["Code"] = clean_code
                    break
        
        # Save to file
        save_to_file(state["Code"], "output/App/main.py")
        
        return state["Code"],1
    

def run_code_iteration(state ) -> str:
        """Run another iteration of code development based on review feedback.""" 
        code = state["Code"]
        review_feedback = state["Code Review"]
        requirements = state.get("Requirement") 
        # Start a conversation with the coding agent for revision
        user_proxy.initiate_chat(
            coding_agent,
            message=f"""Please revise the code based on the review feedback below.
            Ensure all issues are addressed while maintaining compatibility with requirements.
            
            ORIGINAL REQUIREMENTS:
            {requirements}
            
            CURRENT CODE:
            ```python
            {code}
            ```
            
            REVIEW FEEDBACK:
            {review_feedback}
            
            Please provide the revised code that addresses all feedback points.
            """
        )
        
        # Extract the revised code from the conversation
        last_message = coding_agent.last_message()
        revised_code = last_message["content"]
        state["Code"] = revised_code
        # Clean up code (extract from markdown if needed)
        if "```python" in revised_code:
            code_parts = revised_code.split("```python")
            for part in code_parts[1:]:
                if "```" in part:
                    clean_code = part.split("```")[0].strip()
                    revised_code = clean_code
                    break
        
        
        
        # Save to file
        save_to_file(revised_code, "output/App/main.py")
        
        return revised_code,1
    