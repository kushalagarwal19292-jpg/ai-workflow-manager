from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Tool:
    """Represents a tool that an agent can use."""
    name: str
    description: str
    func: Callable[..., Any]

class BaseAgent(ABC):
    """Abstract base class for all specialized agents."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, task_description: str, context: dict) -> str:
        """Executes the agent's specific task."""
        pass

    @abstractmethod
    def can_handle_task(self, task_description: str) -> bool:
        """Determines if the agent is suitable for a given task."""
        pass

print(f"Created {project_root}/agents/base_agent.py")
