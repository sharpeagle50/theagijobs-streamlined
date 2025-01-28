import os
from dotenv import load_dotenv
from crewai import Crew, Task
from agents.agi_leverage_identifier import agi_leverage_identifier
from agents.trainer import trainer
from tasks.identifier_tasks import collect_job_details_task, identify_ai_tools_task
from tasks.trainer_tasks import trainer_task

# Load environment variables
load_dotenv()

# Define Tasks
collect_job_details = Task(
    description="Collect basic job details and a thorough workflow description.",
    expected_output="Job details and workflow description collected.",
    agent=agi_leverage_identifier,
    function=collect_job_details_task,
)

identify_ai_tools = Task(
    description="Analyze the given job's workflow and suggest AI tools.",
    expected_output="A list of AI tools tailored to the job's workflow.",
    agent=agi_leverage_identifier,
    function=lambda: identify_ai_tools_task(
        collect_job_details.function()  # Pass the output of the first task
    ),
    human_input=True
)

trainer_task_instance = Task(
    description="Introduce the identified AI tools and provide a training project.",
    expected_output="Explanations of each AI tool and a basic training project provided.",
    agent=trainer,
    function=trainer_task,
)

# Crew Setup
crew = Crew(
    agents=[agi_leverage_identifier, trainer],
    tasks=[collect_job_details, identify_ai_tools, trainer_task_instance],
    verbose=True
)

if __name__ == "__main__":
    crew.kickoff()
