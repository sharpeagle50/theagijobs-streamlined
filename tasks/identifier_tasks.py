from agents.agi_leverage_identifier import agi_leverage_identifier

# Collect job details and workflow description
def collect_job_details_task():
    print("You are now a company representative.")
    job_details = agi_leverage_identifier.use_tool("request_job_details")
    print(f"Collected Job Details and Workflow Description: {job_details}")
    return job_details

# Suggest AI tools based on workflow
def identify_ai_tools_task(job_details):
    print("\nNow analyzing the job's workflow to suggest AI tools...")
    
    # Extract workflow description from job_details
    workflow_description = job_details.get("Workflow")
    if not workflow_description:
        print("Error: Workflow description is missing.")
        return []

    # Use the workflow description to suggest AI tools
    ai_tools = agi_leverage_identifier.use_tool(
        "suggest_ai_tool", question="Analyze the following workflow and suggest AI tools:", answer=workflow_description
    )
    print(f"Suggested AI Tools: {ai_tools}")
    return ai_tools
