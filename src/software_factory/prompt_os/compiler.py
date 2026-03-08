from typing import Dict, Any
from .templates import CORE_SYSTEM_PROMPT, PLANNER_PROMPT, BUILDER_PROMPT

class PromptCompiler:
    """Dynamically compiles prompts based on agent roles and tasks."""
    
    def __init__(self, role: str):
        self.role = role
        
    def compile(self, task_description: str, context: Dict[str, Any] = None) -> str:
        """Compiles the full prompt string to send to the LLM."""
        base = CORE_SYSTEM_PROMPT
        
        if self.role.lower() == "planner":
            base += f"\n{PLANNER_PROMPT}"
        elif self.role.lower() == "builder":
            base += f"\n{BUILDER_PROMPT}"
            
        compiled = f"{base}\n\nTask: {task_description}"
        if context:
            compiled += f"\n\nContext:\n{context}"
            
        return compiled

