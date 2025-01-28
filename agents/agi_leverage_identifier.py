from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.suggest_ai_tool_tool import SuggestAIToolTool
from tools.request_job_details_tool import RequestJobDetailsTool
import os

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define the Agent
agi_leverage_identifier = Agent(
    role="AGI Leverage Identifier",
    goal="Analyze job workflows and suggest AI tools to optimize them.",
    backstory="An AI expert in workflow optimization.",
    tools=[
        RequestJobDetailsTool(),  # Collects job details and workflow description
        SuggestAIToolTool(),      # Suggests AI tools based on workflow
    ],
    llm=llm
)
