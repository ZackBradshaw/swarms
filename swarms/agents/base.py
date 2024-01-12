from typing import Dict, List

from tool import Tool


class AbstractAgent:
    """(In preview) An abstract class for AI agent.

    An agent can communicate with other agents and perform actions.
    Different agents can differ in what actions they perform in the `receive` method.

    Agents are full and completed:

    Agents = llm + tools + memory


    """

    def __init__(
        self,
        name: str,
        tools: List[Tool],(
        self,
        name: str,
        # tools: List[Tool],
        # memory: Memory
    ):
        """
        Args:
            name (str): name of the agent.
        """
        # a dictionary of conversations, default value is list
        self._name = name

    @property
    def name(self):
        """Get the name of the agent."""
        return self._name

    def reset(self):
        """(Abstract method) Reset the agent."""
        """        """Initialize the tools for the agent."""
        pass

    def reset(self):
        """Reset the agent to its initial state."""
        pass

    def reset(self): """(Abstract method) Reset the agent.""""""(Abstract method) Reset the agent.""""""

    def memory(self, memory_store):
        """init memory"""
        pass

    def reset(self):
        """(Abstract method) Reset the agent."""

    def run(self, task: str):
        """Run the agent once"""

    def _arun(self, taks: str):
        """Run Async run"""

    def chat(self, messages):
        """Chat with the agent"""

    def _achat(self, messages: List[Dict]):
        """Asynchronous Chat"""

    def step(self, message: str):
        """Step through the agent"""

    def _astep(self, message: str):
        """Asynchronous step"""
    def run(self, task):
        """Run the agent once"""
