from typing import Tuple
import autogen
from llm_config import llm_config
from savefile import save_to_file
from agents.User_Proxy_Agent import user_proxy


# Code Review Agent
system_message = """You are a senior code reviewer.
Your job is to:
1. Analyze code for bugs, inefficiencies, and security issues
2. Check code against requirements to ensure all functionality is implemented
3. Evaluate code readability and maintainability
4. Provide specific, actionable feedback
5. Make a clear PASS/REVISION NEEDED decision

Be thorough but fair. Cite specific issues and suggest improvements.
"""

code_review_agent = autogen.AssistantAgent(
    name="CodeReviewer",
    system_message=system_message,
    llm_config=llm_config
)

def run_code_review(state) -> Tuple[bool, str]:
        """Run the code review agent to check code quality."""
        # Start a conversation with the code review agent

        requirements = state["Requirement"]
        code = state["Code"]
        user_proxy.initiate_chat(
            code_review_agent,
            message=f"""Please review the following Python code against the provided requirements.
            Evaluate for correctness, efficiency, readability, and security.
            
            REQUIREMENTS:
            {requirements}
            
            CODE:
            ```python
            {code}
            ```
            
            Please provide detailed feedback and explicitly state if the code PASSES review 
            or NEEDS REVISION. If revision is needed, clearly explain what needs to be fixed.
            """
        )
        
        # Extract the review from the conversation
        last_message = code_review_agent.last_message()
        review_content = last_message["content"]
        state["Code Review"] = review_content
        
        # Determine if the code passed review
        passed = "PASS" in review_content.upper() and "NEEDS REVISION" not in review_content.upper()
        
        
        # Save to file
        save_to_file(review_content, "output/code_review.md")
        
        return passed, review_content,2
    