from abc import ABC, abstractmethod
from typing import Dict, Any, List
from pydantic import BaseModel
import json
from rich.console import Console

from software_factory.core.models import Task, WorkflowPlan, TaskStatus
from software_factory.prompt_os.compiler import PromptCompiler

console = Console()

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.prompt_engine = PromptCompiler(role=self.role)
        
    @abstractmethod
    def execute(self, task: Task, context: Dict[str, Any]) -> str:
        """Executes a task and returns a string result."""
        pass

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Architect", role="planner")
        
    def execute(self, goal: str, context: Dict[str, Any] = None) -> WorkflowPlan:
        console.print(f"[bold cyan]{self.name} (Planner)[/] is analyzing the goal: '{goal}'")
        # In a real implementation this would call an LLM.
        # We mock the plan generation for a UV-installable standalone scaffolding.
        
        plan = WorkflowPlan(
            goal=goal,
            tasks=[
                Task(id="task-1", description="Initialize project directories.", status=TaskStatus.PENDING),
                Task(id="task-2", description="Write core implementation files.", status=TaskStatus.PENDING, dependencies=["task-1"]),
                Task(id="task-3", description="Write README documentation.", status=TaskStatus.PENDING, dependencies=["task-2"])
            ]
        )
        console.print(f"[green]Generated plan with {len(plan.tasks)} tasks.[/]")
        return plan

class BuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="CodeMonkey", role="builder")
        
    def execute(self, task: Task, context: Dict[str, Any] = None) -> str:
        console.print(f"[bold yellow]{self.name} (Builder)[/] is executing task: {task.id}")
        prompt = self.prompt_engine.compile(task.description, context)
        
        # Here we would normally execute tools via LLM tool calling.
        # For now, we simulate execution success.
        console.print(f"[dim]Executing compiled prompt...[/]")
        return f"Simulated success for {task.id}"
