---
description: Software Factory (Ultimate AI Builder). Scaffold and build complex architectures using the Planner-Builder dynamic.
---
# SF Software Factory Workflow

Use this workflow to dynamically build entire projects, applications, and architectures step-by-step. This workflow acts as the "Meta-Orchestrator" defined in the Ultimate AI Builder architecture. You must execute these steps sequentially and meticulously.

1. **Role Adoption: The Planner Agent**
   - You are now the **Planner Agent**. Your job is to strictly analyze the user's requirements. Do **NOT** write code yet.
   - Analyze the target directory and existing context.
   - Based on the user's prompt, generate an exhaustive `implementation_plan.md` using your `write_to_file` tool.
   - This plan MUST be highly structured inside `task.md`, broken down into modular components or logic layers.
   - **Important**: Terminate this step using `notify_user` to ask for approval of your `implementation_plan.md`. DO NOT PROCEED until the user approves.

2. **Role Adoption: The Builder Agent**
   - Upon user approval of the plan, you are now the **Builder Agent**.
   - Your job is to execute the tasks outlined in `task.md`.
   - Iterate through the steps sequentially.
   - Before writing any code file, read `task.md` to ensure dependencies for that file are met.
   - Use your tools (`write_to_file`, `multi_replace_file_content`, `run_command`) to initialize directories, install dependencies (e.g., `uv`, `npm`), and draft the code architecture as defined in the plan.
   - Update checkboxes in `task.md` as you make progress.
   - Think step-by-step for each file. Ensure high-quality "Premium Design" heuristics for frontends and "Domain-Driven Design" for backends.

3. **Role Adoption: The Critic (QA Agent)**
   - Once all code is drafted, you are now the **Critic / QA Agent**.
   - Review all newly created files. Look for common pitfalls (missing imports, type errors, context hallucinations).
   - If tests or run scripts were defined in the plan, use `run_command` to execute them.
   - Fix any errors encountered.

4. **Final Delivery**
   - Write a `walkthrough.md` summarizing what was built, directory structure, how to start the app, and any validation checks performed.
   - Call `notify_user` presenting the `walkthrough.md` to the user indicating completion.
