# Streamlit UI Agent
from typing import Tuple
import autogen
from llm_config import llm_config
from agents.User_Proxy_Agent import user_proxy
from savefile import save_to_file
system_message = """You are a Streamlit UI development expert.
Your job is to:
1. Create intuitive Streamlit UIs for Python applications
2. Develop responsive, user-friendly interfaces
3. Implement proper input validation and error handling
4. Design consistent styling and layout
5. Integrate the UI with the underlying application functionality

Focus on usability, aesthetics, and functional completeness.
"""
ui_agent = autogen.AssistantAgent(
    name="StreamlitUIDesigner",
    system_message=system_message,
    llm_config=llm_config
)

def create_streamlit_ui(state) -> Tuple[bool, str]:
        code = state["Code"]
        user_proxy.initiate_chat(
            ui_agent,
            message=f"""The following is the code of a application.Kindly provide a streamlit UI code that should be easily integrated with the given code.\n
            CODE:
            ```python
            {code}
            ```
            """
        )
        # Extract the review from the conversation
        last_message = ui_agent.last_message()
        streamlit_ui_content = last_message["content"]
        state["Streamlit UI"] = streamlit_ui_content
        # Save to file
        save_to_file(streamlit_ui_content, "output/App/app.py")
        
        return streamlit_ui_content,6