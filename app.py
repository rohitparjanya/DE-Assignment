import os
import shutil
import time
import streamlit as st
import uuid
from agent_pipeline import MultiAgentCodingBot

# Generating session ID
def generate_session_id():
    return str(uuid.uuid4())

# Session state to store user input and session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "text_data" not in st.session_state:
    st.session_state.text_data = ""
if "processing_done" not in st.session_state:
    st.session_state.processing_done = False
if "step_results" not in st.session_state:
    st.session_state.step_results = {}  # Stores results for steps
if "active_tabs" not in st.session_state:
    st.session_state.active_tabs =["Requirement Analysis", "coding", "Code Review", "Documentation","Test Case Generation","Deployment Configuration","Streamlit UI"]  # Stores visible tabs
if "progress" not in st.session_state:
    st.session_state.progress = 0
if "exception" not in st.session_state:
    st.session_state.exception = False

# Page routing
if "page" not in st.session_state:
    st.session_state.page = "home"

# Home Page
if st.session_state.page == "home":
    st.set_page_config(page_title=" Multi-Agentic Coding Bot")
    st.title(":red[Welcome to the Multi-Agentic Coding Bot]")

    # User Input
    user_name = st.text_input("Enter your name:", "")

    if st.button("Submit"):
        if user_name:
            st.session_state.user_name = user_name
            st.session_state.session_id = generate_session_id()
            st.session_state.page = "next"
            st.rerun()  # refresh the page so that next page appears
        else:
            st.error("Please enter your name.")

# Next Page
elif st.session_state.page == "next":
    st.set_page_config(page_title=" Multi-Agentic Coding Bot", layout="wide")
    st.title(f":red[Greetings, {st.session_state.user_name}!]")
    st.session_state.text_data = st.text_area("Enter your Prompt:", st.session_state.text_data, height=150,placeholder="create a calculator app")

    if st.button("Create Application"):
        if st.session_state.text_data.strip():
            st.session_state.processing_done = False
            st.session_state.step_results = {}  # Reset step results
            st.session_state.progress = 0  # Reset progress
            final_state=""
        else:
            st.error("Please enter Prompt")

    
    progress_container = st.empty() 
    status_box = st.empty() 
    
    tabs = st.tabs(st.session_state.active_tabs)
    for i, tab in enumerate(tabs):
        with tab:
            tab.empty()

    final_state=""
    if not st.session_state.processing_done and st.session_state.text_data:
        progress_bar = progress_container.progress(0)
        status = status_box.status("Starting process...",state="running")

        system = MultiAgentCodingBot()
        final_state = system.multiagent_orchestration(st.session_state.text_data,progress_container,tabs,status)
        

        st.session_state.processing_done = True
        
        progress_container.empty()  # Reserve space for progress bar
    
    if st.session_state.processing_done == True and final_state != "Invalid": 
        if os.path.exists("output"):  # Check if folder exists
                shutil.make_archive("processed_data", 'zip', "output")
                with open("processed_data.zip", "rb") as zip_file:
                    st.download_button(
                        label="⬇️ Download Processed Folder",
                        data=zip_file,
                        file_name="processed_data.zip",
                        mime="application/zip",
                    )
        else:
            st.error("❌ Folder not found!")
    # Option to go back
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()