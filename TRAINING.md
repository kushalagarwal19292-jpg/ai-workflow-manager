# Training and Extending Your Agentic AI Business Workflow Manager

This document provides guidelines and instructions on how to train or fine-tune your specialized AI agents, update their skills, and connect them to new external tools, ensuring your workflow manager remains adaptable and powerful.

## 1. Training and Fine-Tuning Agents

Training and fine-tuning are crucial for maximizing the performance and domain-specificity of your AI agents. This primarily applies to the underlying Large Language Models (LLMs) used by agents.

### General Approach for Fine-Tuning LLMs:
1.  **Identify the Target Agent and Task**: Determine which agent (e.g., `RagAgent`, `SalesAgent`) needs performance improvement for a specific task (e.g., better sales lead qualification, more accurate document summaries).
2.  **Collect Domain-Specific Data**: Gather a dataset relevant to the agent's task and your organization's specific context. This data should reflect the desired output and style.
3.  **Prepare the Data**: Format the collected data into a suitable structure for fine-tuning (e.g., question-answer pairs for RAG, structured sales interaction logs, policy documents for compliance).
4.  **Choose a Fine-Tuning Method**: Decide between full fine-tuning (adjusting all model parameters) or more efficient methods like LoRA (Low-Rank Adaptation) if supported by your LLM provider.
5.  **Execute Fine-Tuning**: Use your chosen LLM provider's (e.g., OpenAI, AWS) API or a library like Hugging Face `transformers` to perform the fine-tuning.
6.  **Evaluate the Fine-Tuned Model**: Test the new model rigorously against a held-out validation set to ensure it meets performance requirements and avoids overfitting.

### Steps for Fine-Tuning a Specific Agent (Example: `SalesAgent`)

Let's consider fine-tuning a `SalesAgent` to improve lead qualification accuracy:

1.  **Data Collection**: Collect historical sales data, including lead profiles, interaction logs, conversion outcomes, and successful/unsuccessful lead characteristics.
2.  **Data Preparation**: Structure the data into prompt-completion pairs or classification examples. For instance:
    *   **Prompt**: `"Lead details: Company X, Industry Y, Contact Z, Recent engagement: [engagement details]. Score this lead (High/Medium/Low)."`
    *   **Completion**: `"High"` (or `"Medium"`, `"Low"`)
3.  **Fine-tuning Execution**: Use the OpenAI Fine-tuning API (or a similar service) to fine-tune a base LLM model on your prepared dataset.
    *   `openai.fine_tuning.jobs.create(model="gpt-3.5-turbo", training_file="file-xxxxxx")`
4.  **Integration**: Update the `SalesAgent`'s internal logic to use the new fine-tuned model ID.
    *   ```python
        # Inside SalesAgent's __init__ or a method
        self.llm = OpenAI(model_name="ft:gpt-3.5-turbo:your-org::xxxxxx")
        ```
5.  **Evaluation**: Monitor the `SalesAgent`'s performance in a staging environment, tracking lead qualification accuracy and feedback from sales teams.

### Tools/Libraries for Fine-Tuning:
-   **OpenAI Fine-tuning APIs**: For fine-tuning GPT models.
-   **Hugging Face Ecosystem**: Libraries like `transformers` and `peft` (for LoRA) are excellent for open-source LLMs.
-   **LangChain**: Can integrate fine-tuned models seamlessly into agents and workflows.

## 2. Updating Agent Skills

Agents can be enhanced by adding new skills or modifying existing ones. This involves updating their internal `Tool` definitions and `can_handle_task` logic.

### Steps to Add a New Skill (e.g., 'Generate Sales Proposal Outline' to `SalesAgent`):

1.  **Define the New `Tool`**: Create a function that encapsulates the new skill (e.g., generating a sales proposal outline) and define it as a `Tool` dataclass instance.
    *   **Example Tool Function** (`utils/sales_tools.py`):
        ```python
        def generate_proposal_outline(client_name: str, scope: str) -> str:
            # Logic to generate a detailed proposal outline
            return f"Outline for {client_name} proposal on {scope}: ..."
        ```
    *   **Example `Tool` Definition** (inside `SalesAgent` or passed to it):
        ```python
        from agents.base_agent import Tool
        from utils.sales_tools import generate_proposal_outline
        
        proposal_tool = Tool(
            name="GenerateProposalOutline",
            description="Generates a structured outline for a sales proposal given client and scope.",
            func=generate_proposal_outline
        )
        ```
2.  **Integrate with Existing Agent Logic**: Make the `SalesAgent` aware of this new tool. This might involve adding it to a list of `self.tools` within the agent's `__init__`.
3.  **Update `can_handle_task`**: Modify the `SalesAgent`'s `can_handle_task` method to recognize task descriptions that require this new skill.
    *   ```python
        def can_handle_task(self, task_description: str) -> bool:
            keywords = ["sales", "lead", "proposal outline", "crm"]
            return any(keyword in task_description.lower() for keyword in keywords)
        ```
4.  **Update `run` Method**: Implement logic within the `SalesAgent`'s `run` method to call the `generate_proposal_outline` tool when appropriate.
    *   ```python
        def run(self, task_description: str, context: dict) -> str:
            if "proposal outline" in task_description.lower():
                client = context.get("client_name")
                scope = context.get("scope")
                if client and scope:
                    return self.proposal_tool.func(client, scope)
            # ... existing sales agent logic ...
            return "Sales operation executed."
        ```

## 3. Connecting New External Tools

Integrating new external services or APIs allows agents to access a broader range of functionalities (e.g., project management software, HR systems).

### Steps to Connect a New External Tool (Example: 'Jira API' for `ComplianceAgent`):

1.  **Identify the Need**: A `ComplianceAgent` might need to create/update Jira tickets for audit findings.

2.  **Implement an Integration Utility**: Create a new Python module (e.g., `utils/jira_integration.py`) that handles authentication and API calls to Jira.
    *   ```python
        # utils/jira_integration.py
        import requests
        from config.config import JIRA_API_KEY, JIRA_URL
        
        def create_jira_issue(project_key: str, summary: str, description: str) -> str:
            headers = {"Authorization": f"Bearer {JIRA_API_KEY}", "Content-Type": "application/json"}
            data = {"fields": {"project": {"key": project_key}, "summary": summary, "description": description, "issuetype": {"name": "Task"}}}
            response = requests.post(f"{JIRA_URL}/rest/api/2/issue", headers=headers, json=data)
            response.raise_for_status()
            return response.json()["key"]
        ```

3.  **Update Agent `__init__`**: Modify the `ComplianceAgent`'s constructor to accept the Jira client/API as a dependency. Also, update `config/config.py` with `JIRA_API_KEY` and `JIRA_URL`.
    *   ```python
        # agents/compliance_agent.py
        from utils.jira_integration import create_jira_issue
        
        class ComplianceAgent(BaseAgent):
            def __init__(self, name: str, description: str, compliance_tool: Any = None, jira_client: Any = None):
                super().__init__(name, description)
                self.compliance_tool = compliance_tool
                self.jira_client = jira_client # Now injected
        ```

4.  **Integrate in `run` Method**: Call the new integration utility from the `ComplianceAgent`'s `run` method when the task requires it.
    *   ```python
        def run(self, task_description: str, context: dict) -> str:
            if "create jira ticket" in task_description.lower() and self.jira_client:
                project = context.get("jira_project", "COMPLIANCE")
                summary = context.get("ticket_summary", task_description)
                description = context.get("ticket_description", "Automated compliance finding.")
                ticket_key = self.jira_client(project, summary, description) # Assuming jira_client is the create_jira_issue function
                return f"Jira ticket {ticket_key} created for compliance finding."
            return f"Compliance check executed for: {task_description}"
        ```

5.  **Testing**: Thoroughly test the new Jira integration, preferably in a sandbox environment, to ensure issues are created correctly and securely.

## 4. Best Practices for Training and Integration

-   **Data Quality**: Always prioritize high-quality, relevant, and diverse training data. Poor data leads to poor model performance.
-   **Version Control**: Use version control for your datasets, models, and agent code. This allows for reproducibility and easier rollback.
-   **Monitoring**: Implement robust monitoring for agent performance, API usage, and error rates in production. This helps in identifying degradation or issues quickly.
-   **Security**: Handle all API keys, credentials, and sensitive data securely. Use environment variables (via `config.py`) or a secrets management service. Never hardcode sensitive information.
-   **Iterative Development**: Agent development and training are iterative processes. Start small, test, gather feedback, and gradually expand capabilities.

## 5. Example: Adding a 'Document Creation' Skill to an Agent

Imagine you want an agent to generate outlines for new internal documents (e.g., SOPs, policy updates).

1.  **New Agent/Skill**: You could enhance an existing `RAG Agent` or create a new `DocumentationAgent`.
2.  **Tool Function**: Create a function `generate_document_outline(doc_type: str, topic: str) -> str` that uses an LLM to craft an outline.
3.  **Integration**: Add this function as a `Tool` to the chosen agent. The agent's `can_handle_task` method would recognize phrases like "draft outline for SOP" or "create policy draft structure". The `run` method would then invoke the `generate_document_outline` tool.
4.  **Prompt Engineering**: Use meta-prompting to guide the LLM within the `generate_document_outline` function, providing examples of good outlines for different document types.
