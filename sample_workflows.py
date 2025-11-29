from typing import Dict, Any

from workflows.orchestrator import Orchestrator
from agents.rag_agent import RagAgent
from agents.tag_agent import TagAgent
from agents.email_agent import EmailAgent
from agents.compliance_agent import ComplianceAgent
from agents.sales_agent import SalesAgent
from agents.hr_agent import HRAgent

def run_lead_scoring_workflow():
    print("\n--- Running Lead Scoring Workflow ---")
    sales_agent = SalesAgent(name="LeadScorer", description="Agent for scoring and qualifying leads.")
    orchestrator = Orchestrator(agents=[sales_agent])
    task = "Score the lead 'Acme Corp' with contact 'Jane Doe' based on recent engagement data."
    context = {"lead_name": "Acme Corp", "contact_person": "Jane Doe"}
    result = orchestrator.run_workflow(task, context)
    print(f"Lead Scoring Workflow Result: {result}")

def run_invoice_extraction_workflow():
    print("\n--- Running Invoice Extraction Workflow ---")
    # In a real scenario, an OCR agent would be involved here, but for this mock, TAG agent can simulate data processing.
    tag_agent = TagAgent(name="InvoiceProcessor", description="Agent for extracting and processing invoice data.")
    orchestrator = Orchestrator(agents=[tag_agent])
    task = "Extract line items and total amount from invoice INV-2023-001."
    context = {"invoice_id": "INV-2023-001", "document_path": "data/invoices/inv-001.pdf"}
    result = orchestrator.run_workflow(task, context)
    print(f"Invoice Extraction Workflow Result: {result}")

def run_hr_screening_workflow():
    print("\n--- Running HR Screening Workflow ---")
    hr_agent = HRAgent(name="CandidateScreener", description="Agent for screening job applicants.")
    orchestrator = Orchestrator(agents=[hr_agent])
    task = "Screen candidate 'Alice Smith' for the 'Software Engineer' position based on resume 'alice_resume.pdf'."
    context = {"candidate_name": "Alice Smith", "position": "Software Engineer", "resume_file": "alice_resume.pdf"}
    result = orchestrator.run_workflow(task, context)
    print(f"HR Screening Workflow Result: {result}")

def run_data_cleaning_workflow():
    print("\n--- Running Data Cleaning Workflow ---")
    tag_agent = TagAgent(name="DataCleaner", description="Agent for cleaning and harmonizing data.")
    orchestrator = Orchestrator(agents=[tag_agent])
    task = "Clean and deduplicate the 'customer_data.csv' spreadsheet."
    context = {"dataset": "customer_data.csv", "operation": "clean_deduplicate"}
    result = orchestrator.run_workflow(task, context)
    print(f"Data Cleaning Workflow Result: {result}")

def run_customer_ticket_routing_workflow():
    print("\n--- Running Customer Ticket Routing Workflow ---")
    rag_agent = RagAgent(name="TicketClassifier", description="Agent for classifying and routing customer tickets.")
    email_agent = EmailAgent(name="TicketResponder", description="Agent for drafting and sending email replies.")
    orchestrator = Orchestrator(agents=[rag_agent, email_agent])
    task = "Route customer support ticket 'CT-9876' concerning a 'product return' and draft an initial response."
    context = {"ticket_id": "CT-9876", "issue_summary": "Product return inquiry"}
    result = orchestrator.run_workflow(task, context)
    print(f"Customer Ticket Routing Workflow Result: {result}")

if __name__ == "__main__":
    print("Running sample workflows...")
    run_lead_scoring_workflow()
    run_invoice_extraction_workflow()
    run_hr_screening_workflow()
    run_data_cleaning_workflow()
    run_customer_ticket_routing_workflow()
    print("All sample workflows completed.")

print(f"Created {project_root}/workflows/sample_workflows.py")
