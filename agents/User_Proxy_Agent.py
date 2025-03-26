import autogen

# user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=0,
    system_message="You are a user who needs a software solution. You provide requirements and review the final outputs.",
    code_execution_config={"use_docker": False},
)


