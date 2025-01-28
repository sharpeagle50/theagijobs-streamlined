from crewai.tools import BaseTool

class RequestJobDetailsTool(BaseTool):
    name: str = "request_job_details"
    description: str = "Collects basic job details and a detailed workflow description from the company representative."

    def _run(self):
        job_details = {
            "Title": input("What is the job title? ").strip(),
            "Salary Range": input("What is the salary range? ").strip(),
            "Prerequisites": input("What are the prerequisites for this position? ").strip(),
            "Workflow": input("Please provide a thorough explanation of the job's workflow: ").strip(),
        }
        print(f"DEBUG: Collected Job Details: {job_details}")
        return job_details
