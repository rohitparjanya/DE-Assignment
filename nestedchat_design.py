from autogen import ConversableAgent
from llm_config import llm_config

user_proxy = ConversableAgent(
    name="user_proxy",
    llm_config = False,
    is_termination_msg = lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode = "NEVER"
)

# req analysis
system_message = """You are a requirement analysis expert. 
Your job is to:
1. Take natural language requirements
2. Structure them into clear, detailed software requirements
3. Identify any ambiguities or missing details and resolve them
4. Organize requirements into functional, non-functional, and technical categories
5. Output a JSON format with the structured requirements

Your response should be clear, thorough, and actionable for the coding team.
Return "TERMINATE" when the task is done.
"""
req_analysis_agent = ConversableAgent(
    name="RequirementAnalyst",
    system_message=system_message,
    llm_config=llm_config,
    
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1
)


# coding agent
system_message = """You are an expert Python developer.
Your job is to:
1. Take structured requirements
2. Develop clean, efficient, and modular Python code that satisfies all requirements
3. Use best practices and design patterns
4. Provide explanatory comments
5. Handle edge cases and errors appropriately

If your code is sent back for revision, carefully analyze the feedback and improve accordingly.
Return "TERMINATE" when the task is done.
"""
coding_agent = ConversableAgent(
    name="CodeDeveloper",
    system_message=system_message,
    llm_config=llm_config,
    
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1
)



# Code Review Agent
system_message = """You are a senior code reviewer.
Your job is to:
1. Analyze code for bugs, inefficiencies, and security issues
2. Check code against requirements to ensure all functionality is implemented
3. Evaluate code readability and maintainability
4. Provide specific, actionable feedback
5. Make a clear PASS/REVISION NEEDED decision

Be thorough but fair. Cite specific issues and suggest improvements.
Return "TERMINATE" when the task is done.
"""

code_review_agent = ConversableAgent(
    name="CodeReviewer",
    system_message=system_message,
    llm_config=llm_config,
    
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1
)


# Documentation Agent
system_message = """You are a documentation specialist.
Your job is to:
1. Create comprehensive documentation for Python code
2. Follow standard documentation formats
3. Include overview, installation instructions, usage examples, and API references
4. Ensure documentation is clear for both technical and non-technical users
5. Use Markdown format for the documentation

Focus on clarity, completeness, and usability.
Return "TERMINATE" when the task is done.
"""
doc_agent = ConversableAgent(
    name="DocumentationSpecialist",
    system_message=system_message,
    llm_config=llm_config,
    
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1
)


# testcase gen
system_message = """You are a test engineering expert.
Your job is to:
1. Generate comprehensive test cases for Python code
2. Write both unit tests and integration tests using pytest
3. Ensure high test coverage
4. Include edge cases and error handling tests
5. Develop test fixtures and setup/teardown as needed

Make tests thorough, maintainable, and descriptive.
Return "TERMINATE" when the task is done.
"""

test_agent = ConversableAgent(
    name="TestEngineer",
    system_message=system_message,
    llm_config=llm_config,
    
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1
)


# StreamlitUI agent
system_message = """You are a Streamlit UI development expert.
Your job is to:
1. Create intuitive Streamlit UIs for Python applications
2. Develop responsive, user-friendly interfaces
3. Implement proper input validation and error handling
4. Design consistent styling and layout
5. Integrate the UI with the underlying application functionality

Focus on usability, aesthetics, and functional completeness.

Return "TERMINATE" when the task is done.
"""
ui_agent = ConversableAgent(
    name="StreamlitUIDesigner",
    system_message=system_message,
    llm_config=llm_config,
    
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1
)



# creating a nested chat 
coding_agent.register_nested_chats(
    trigger=user_proxy,
    chat_queue=[
        {
            "sender":code_review_agent,
            "recipient":coding_agent,
            "summary_method":"last_msg",
            "max_turns":2
        }
    ]
)


chat_results = user_proxy.initiate_chats(
    [
        {
            "recipient":req_analysis_agent,
            "message":"Create a simple random number generator app",
            "summary_method": "last_msg"
        },
        {
            "recipient":coding_agent,
            "message":"""You are an expert Python developer.
                    Your job is to:
                    1. Take structured requirements
                    2. Develop clean, efficient, and modular Python code that satisfies all requirements
                    3. Use best practices and design patterns
                    4. Provide explanatory comments
                    5. Handle edge cases and errors appropriately

                    If your code is sent back for revision, carefully analyze the feedback and improve accordingl""",
            "summary_method": "last_msg"
        },
        {
            "recipient":doc_agent,
            "message":"""You are a documentation specialist.
                    Your job is to:
                    1. Create comprehensive documentation for Python code
                    2. Follow standard documentation formats
                    3. Include overview, installation instructions, usage examples, and API references
                    4. Ensure documentation is clear for both technical and non-technical users
                    5. Use Markdown format for the documentation

                    Focus on clarity, completeness, and usability.
                    """,
            "summary_method": "last_msg"
        },
        {
            "recipient":test_agent,
            "message":"""You are a test engineering expert.
                    Your job is to:
                    1. Generate comprehensive test cases for Python code
                    2. Write both unit tests and integration tests using pytest
                    3. Ensure high test coverage
                    4. Include edge cases and error handling tests
                    5. Develop test fixtures and setup/teardown as needed

                    Make tests thorough, maintainable, and descriptive.
                    """,
            "summary_method": "last_msg"
        },
        {
            "recipient":ui_agent,
            "message": """You are a Streamlit UI development expert.
                    Your job is to:
                    1. Create intuitive Streamlit UIs for Python applications
                    2. Develop responsive, user-friendly interfaces
                    3. Implement proper input validation and error handling
                    4. Design consistent styling and layout
                    5. Integrate the UI with the underlying application functionality

                    Focus on usability, aesthetics, and functional completeness.
                    """,
            "summary_method": "last_msg"
        }
    ]
)

