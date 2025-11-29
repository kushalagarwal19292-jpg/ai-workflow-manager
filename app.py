import streamlit as st
import asyncio
import logging
import os

# Import agents and orchestrator
from workflows.orchestrator import Orchestrator
from agents.rag_agent import RagAgent
from agents.tag_agent import TagAgent
from agents.email_agent import EmailAgent
from agents.compliance_agent import ComplianceAgent
from agents.sales_agent import SalesAgent
from agents.hr_agent import HRAgent

# Import utility for real-time execution
from utils.realtime_utils import async_run_task

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set Streamlit page config
st.set_page_config(page_title="Agentic AI Workflow Manager", layout="wide")

def init_orchestrator():
    # Initialize mock agents (real agents would have actual dependencies injected)
    rag_agent = RagAgent(name="RAG Agent", description="Retrieves information from knowledge bases.", vector_store=None, retriever=None)
    tag_agent = TagAgent(name="TAG Agent", description="Processes and analyzes tabular data.", db_connector=None)
    email_agent = EmailAgent(name="Email Agent", description="Manages email communications.", email_client=None)
    compliance_agent = ComplianceAgent(name="Compliance Agent", description="Ensures regulatory adherence and audits.", compliance_tool=None)
    sales_agent = SalesAgent(name="Sales Agent", description="Handles sales-related tasks like lead scoring.", crm_api=None)
    hr_agent = HRAgent(name="HR Agent", description="Manages HR processes like candidate screening.", hr_system_api=None)

    agents = [rag_agent, tag_agent, email_agent, compliance_agent, sales_agent, hr_agent]
    return Orchestrator(agents=agents)

# Initialize orchestrator once
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = init_orchestrator()

orchestrator = st.session_state.orchestrator

async def run_workflow_streamlit(task_description: str, orch: Orchestrator):
    """Runs the workflow and handles Streamlit display."""
    try:
        # Simulate asynchronous execution using async_run_task
        result = await async_run_task(orch.run_workflow, task_description)
        return result
    except Exception as e:
        logger.error(f"Error running workflow: {e}")
        return f"An error occurred: {e}"


# Streamlit UI
st.title("🤖 Agentic AI Business Workflow Manager")
st.markdown("Automate and manage your business workflows with specialized AI agents.")

task_description = st.text_area(
    "Enter your task description:",
    "Example: 'Retrieve the latest sales report for Q1 2024 and email it to stakeholders.'",
    height=100
)

if st.button("Trigger Workflow"):
    if task_description:
        with st.spinner("Running workflow... Please wait."):
            try:
                # Run the asynchronous workflow
                workflow_output = asyncio.run(run_workflow_streamlit(task_description, orchestrator))
                st.success(f"Workflow completed!\n\nResult: {workflow_output}")
            except ValueError as ve:
                st.error(f"Workflow Error: {ve}")
            except Exception as e:
                st.error(f"An unexpected error occurred during workflow execution: {e}")
    else:
        st.warning("Please enter a task description to trigger a workflow.")


print(f"Created {project_root}/app.py")
