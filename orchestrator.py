from typing import List, Dict, Any
from agents.base_agent import BaseAgent

class Orchestrator:
    """Central manager for delegating tasks and coordinating agent workflows."""

    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.history = [] # To keep track of conversation/task history

    def select_agent(self, task_description: str) -> BaseAgent:
        """Selects the most suitable agent for the given task based on their can_handle_task method."""
        for agent in self.agents:
            if agent.can_handle_task(task_description):
                print(f"Orchestrator: Selected {agent.name} for task: {task_description[:50]}...")
                return agent
        raise ValueError(f"No suitable agent found for task: {task_description}")

    def run_workflow(self, initial_task: str, context: Dict[str, Any] = None) -> str:
        """Executes a task by selecting and delegating to an agent, and records the interaction."""
        if context is None:
            context = {}

        print(f"\nOrchestrator: Starting workflow for task: {initial_task}")
        self.history.append({"role": "user", "content": initial_task})

        try:
            selected_agent = self.select_agent(initial_task)
            result = selected_agent.run(initial_task, context)
            self.history.append({"role": "agent", "name": selected_agent.name, "content": result})
            print(f"Orchestrator: Workflow completed by {selected_agent.name}. Result: {result[:100]}...")
            return result
        except ValueError as e:
            self.history.append({"role": "error", "content": str(e)})
            print(f"Orchestrator: Workflow failed - {e}")
            return f"Error: {e}"

print(f"Created {project_root}/workflows/orchestrator.py")
