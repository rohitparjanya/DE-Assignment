import autogen
import os
from typing import Dict
from agents.Code_Review_Agent import run_code_review
from agents.Deployment_Configuration_Agent import run_deployment_config_generator
from agents.Documentation_Agent import run_documentation_generation
from agents.Requirement_Analysis_Agent import run_requirement_analysis
from agents.Streamlit_UI_Agent import create_streamlit_ui
from agents.Test_Case_Generation import generate_testcases
from agents.User_Prompt_Validation_Agent import validate_prompt
from agents.coding_Agent import run_code_development, run_code_iteration



class MultiAgentCodingBot:
    def __init__(self):
        # Create output directories
        os.makedirs("output", exist_ok=True)
        os.makedirs("output/App", exist_ok=True)
        

        # Initialize conversation state
        self.state = {
            "Requirement": "",
            "Requirement Analysis": "",
            "Code": "",
            "Documentation": "",
            "Test Case Generation": "",
            "Streamlit UI": "",
            "Code Review": "",
            "Deployment Configuration": "",
            "review_passed": False
        }
        
    def multiagent_orchestration(self, user_given_prompt: str,progress_bar,tabs,status) -> Dict:
        # Store the original requirement
        self.state["Requirement"] = user_given_prompt

        valid,analysis_report = validate_prompt(self.state)
        if not valid:
            status.update(label=analysis_report, state="error")
            return "Invalid"
        
        try:
            status.update(label="Requirement analysis phase is in progress", state="running")
            user_prompt,idx = run_requirement_analysis(self.state)
            status.update(label="Requirement analysis phase is Completed ✅", state="complete")
            progress_bar.progress(int(((idx+1)/7)*100))
            tabs[idx].write(user_prompt)
        except Exception as e:
            print("exception occured at requirement analysis :",e)
            status.update(label="Requirement analysis phase is failed", state="error")
            return ""



        try:
            status.update(label="code generation is in progress", state="running")
            code,idx = run_code_development(self.state)
            progress_bar.progress(int(((idx+1)/7)*100))
            status.update(label="code generation is Completed ✅", state="complete")
            tabs[idx].write(code)
        except Exception as e:
            print("exception occured at code generation:",e)
            status.update(label="code generation failed", state="error")
            return ""
        

        
        # Step 3: Code Review (and potential iterations)
        max_iterations = 3
        iteration = 0
        passed = False
        
        while not passed and iteration < max_iterations:
            try:
                status.update(label="code review is in progress", state="running")
                passed, review_feedback,idx = run_code_review(self.state)
                progress_bar.progress(int(((idx+1)/7)*100))
                status.update(label="code review is Completed ✅", state="complete")
                tabs[idx].write(review_feedback)
                
                self.state["review_passed"] = passed
                
                if not passed:
                    try:
                        status.update(label="code review phase is not passed. suggested code generater agent to regenerate code", state="running")
                        code,idx = run_code_iteration(self.state)
                        status.update(label="code re-generated successfully ✅", state="complete")
                        progress_bar.progress(int(((idx+1)/7)*100))
                        tabs[idx].write(code)
                        iteration += 1
                    except Exception as e:
                        print("exception occured at code re-generation :",e)
                        status.update(label="code re-generation failed", state="error")
                        return ""
                else:
                    print("System", "Code review passed!")
            except Exception as e:
                print("exception occured at code review:",e)
                status.update(label="code review failed", state="error")
                return ""
        
        # If still not passed after max iterations, we proceed anyway
        if not passed:
            status.update(label=f"Code reviewed {max_iterations} times. Moving forward with documentation..", state="running")
            print("System", f"Code reviewed {max_iterations} times. Moving forward with documentation..")
        
        # Step 4: Documentation Generation
        try:
            status.update(label="document generation is in progress", state="running")
            documentation,idx = run_documentation_generation(self.state)
            progress_bar.progress(int(((idx+1)/7)*100))
            tabs[idx].write(documentation)
            status.update(label="document generation is complete ✅", state="complete")
        except Exception as e:
            print("exception occured at document generation:",e)
            status.update(label="document generation failed", state="error")
            return ""
        
        # Step 5: Test Generation
        try:
            status.update(label="testcase generation is in progress", state="running")
            testcases,idx = generate_testcases(self.state)
            progress_bar.progress(int(((idx+1)/7)*100))
            tabs[idx].write(testcases)
            status.update(label="testcase generation is complete ✅", state="complete")
        except Exception as e:
            print("exception occured at testcase generation:",e)
            status.update(label="testcase generation failed", state="error")
            return ""
        

        # Step 6: deployment Config
        try:
            status.update(label="deployment configuration generation is in progress", state="running")
            deployment_config,idx = run_deployment_config_generator(self.state)
            progress_bar.progress(int(((idx+1)/7)*100))
            tabs[idx].write(deployment_config)
            status.update(label="deployment configuration is complete ✅", state="complete")
        except Exception as e:
            print("exception occured at deployment configuration:",e)
            status.update(label="deployment configuration failed", state="error")
            return ""
        
        # Step 7: Streamlit UI Generation
        try:
            status.update(label="streamlit UI generation is in progress", state="running")
            streamlit_ui_code,idx = create_streamlit_ui(self.state)
            progress_bar.progress(int(((idx+1)/7)*100))
            tabs[idx].write(streamlit_ui_code)
            status.update(label="streamlit UI generation is complete ✅", state="complete")
        except Exception as e:
            print("exception occured at streamlit UI generation:",e)
            status.update(label="streamlit UI generation failed", state="error")
            return ""
        
        return {
            "Requirement": user_given_prompt,
            "Requirement Analysis": user_prompt,
            "Code": code,
            "Documentation": documentation,
            "Test Case Generation": testcases,
            "Streamlit UI": streamlit_ui_code,
            "Code Review": review_feedback,
            "Deployment Configuration": deployment_config,
            "review_passed": passed
        }

