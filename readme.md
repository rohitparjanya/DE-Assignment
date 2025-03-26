# Multi-Agent Coding Bot

A collaborative AI system that transforms natural language requirements into fully functional Python code using specialized agents.

## Overview
This project showcases an innovative Multi-Agentic Framework powered by AutoGen, where specialized agents collaborate seamlessly to bring software to life from natural language requirements. The system includes:
**Requirement Analysis Agent**: Skillfully converts natural language into well-structured software requirements.
**Coding Agent**: Transforms these requirements into fully functional Python code with precision.
**Code Review Agent**: Ensures code correctness, efficiency, and robust security through meticulous review.
**Documentation Agent**: Crafts comprehensive and clear documentation to accompany the software.
**Test Case Generation Agent**: Develops thorough unit and integration tests to guarantee reliability.
**Deploy Config Generator Agent**: Provides the suitable config for robust deployement.
**Streamlit UI Agent**: Designs an intuitive user interface for the system, enhancing accessibility.

The agents work collaboratively in a pipeline, with each agent's output feeding into the next agent in the workflow.

## Architecture
The system consists of multiple agents, each responsible for a specific task. The overall flow is as follows:
**User Proxy Agent**: This agent serves as the entry point, taking input from the user and initializing the processing pipeline.
**State Management**: A class is initialized to maintain the state of the conversation, storing intermediate outputs from agents for use by subsequent agents.
**Orchestration Function**: This function coordinates interactions between agents, ensuring that responses are passed to the next agent in sequence.
**Coding Agent**: Generates code based on the given prompt or requirements.
**Code Review Agent**: Reviews the generated code and determines if it meets the required quality and correctness.
**Re-execution Mechanism**: If the review agent finds issues, it prompts the coding agent to regenerate or modify the code.
**Sequential Processing**: Once the review is passed, the pipeline continues sequentially to other agents.


## Code structure
```
DE-Assignment/
│
├── app.py                  # Streamlit UI for the multi-agent coding bot
├── agent_pipeline.py       # creating a sequence pipeline to execute the multi agent coding system
├── requirements.txt        # required libraries
├── .env                    # Environment variables file (create this and add GROQ_API_KEY)
├── llm_config.py           # Configuring the models like llama,gpt-4o etc
├── savefile.py             # saves content to a file
│── readme.md
└── agents/                 # all the agents are created here
    ├── User_Proxy_Agent.py   
    ├── User_Propmt_Validation.py   
    ├── Requirement_Analysis_Agent.py   
    ├── Coding_Agent.py   
    ├── Code_Review_Agent.py   
    ├── Documentation_Agent.py   
    ├── Test_Case_Generation.py   
    ├── Deployement_Configuration_Agent.py   
    └── Streamlit_UI_Agent.py
└── output/                 # Generated outputs (created automatically)
    ├── App/                # Root folder for code
    └── docs/               # Generated documentation
```

## Key Features

- **Iterative Processing**: If code fails review, it's sent back to the Coding Agent for improvements
- **LLM Integration**: Support for multiple LLM providers (OpenAI, Groq)
- **User-Friendly Interface**: Streamlit UI for interaction with the system
- **Comprehensive Documentation**: Generated automatically for the developed code
- **Test Case Generation**: Creates unit and integration tests for the code

## Installation & Setup

1. Clone the repository:
   git clone https://github.com/rohitparjanya/DE-Assignment.git
   cd DE-Assignment

2. Create virtual env:
   python -m venv .venv
   .venv/Scripts/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set Environment Variables  in .env
   Add environment variables:
    - `OPENAI_API_KEY`: Your OpenAI API key
    - `GROQ_API_KEY`: Your Groq API key
  
5. Run the Streamlit app:
   streamlit run app.py

## Usage

1. Access the Streamlit interface at http://localhost:8501
2. Provide the name
3. Click on "submit" to redirect to Dashboard page
4. Provide the prompt
5. Click on "Create Application" to start the process
5. View the progess and dynamically check the populated tabs
   - Requirement Analysis - coding - Code Review - Documentation - Test Case Generation - Deployment Configuration - Streamlit UI



## Technical Requirements

- Python 3.11.3
- Internet connection for LLM API access
- OpenAI or Groq cloud API credentials or open-api Key


