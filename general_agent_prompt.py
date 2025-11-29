GENERAL_AGENT_PROMPT_TEMPLATE = """
You are a helpful AI assistant. Your goal is to process the given task description, considering the conversation history.

Conversation History:
{history}

Task Description:
{task_description}

Provide a detailed and actionable response to the task.
"""

print(f"Created {project_root}/prompts/general_agent_prompt.py")
