from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class Task(BaseModel):
    id: str = Field(..., description="Unique identifier for the task at hand.")
    description: str = Field(..., description="A detailed description of the task to be executed.")
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    dependencies: List[str] = Field(default_factory=list, description="IDs of tasks that must complete before this one.")
    result: Optional[str] = None

class WorkflowPlan(BaseModel):
    goal: str = Field(..., description="The overall goal.")
    tasks: List[Task] = Field(default_factory=list, description="The sequential/parallel tasks to achieve the goal.")

class ExecutionState(BaseModel):
    plan: Optional[WorkflowPlan] = None
    memory: Dict[str, Any] = Field(default_factory=dict)
