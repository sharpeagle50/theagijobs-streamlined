from agents.trainer import trainer

def trainer_task(ai_tools):
    print("\nTrainer: Hello applicant, you are now talking to our AI trainer.")
    print(f"It will train you on the following tools: {', '.join(ai_tools)}.")
    print("Let me provide you with some information and exercises to get started.")

    # Explain each tool
    for tool in ai_tools:
        print(f"\nTrainer: Let’s discuss the tool '{tool}'.")
        prompt = (
            f"You are training a job applicant. Explain the AI tool '{tool}' in 1-2 sentences. "
            f"Highlight its functionality and practical use cases."
        )
        response = trainer.llm.invoke([{"role": "system", "content": prompt}])
        print(f"- {tool}: {response.content.strip()}")

    # Generate a practice project
    tools_list = ', '.join(ai_tools)
    project_prompt = (
        f"Create a practice project for a job applicant using these AI tools: {tools_list}. "
        f"Ensure the project provides practical experience relevant to the job role."
    )
    project_response = trainer.llm.invoke([{"role": "system", "content": project_prompt}])
    print("\nTrainer: Here's a practice project to help you master the tools:\n")
    print(project_response.content.strip())
