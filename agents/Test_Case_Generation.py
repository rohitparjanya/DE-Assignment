# Test Case Generation Agent
from typing import Tuple
import autogen
from llm_config import llm_config
from agents.User_Proxy_Agent import user_proxy
from savefile import save_to_file

system_message = """You are a test engineering expert.
Your job is to:
1. Generate comprehensive test cases for Python code
2. Write both unit tests and integration tests using pytest
3. Ensure high test coverage
4. Include edge cases and error handling tests
5. Develop test fixtures and setup/teardown as needed

Make tests thorough, maintainable, and descriptive.
"""

test_agent = autogen.AssistantAgent(
    name="TestEngineer",
    system_message=system_message,
    llm_config=llm_config
)

def generate_testcases(state) -> Tuple[bool, str]:
        code = state["Code"]
        user_proxy.initiate_chat(
            test_agent,
            message=f"""The following is the code of a application.You should provide the testcase file suitable for the given code.\n
            CODE:
            ```python
            {code}
            ```
            """
        )
        # Extract the review from the conversation
        last_message = test_agent.last_message()
        tescases_content = last_message["content"]
        state["Test Case Generation"] = tescases_content
        # Save to file
        save_to_file(tescases_content, "output/testcases.py")
        
        return tescases_content,4