from crewai import Agent
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Define the Trainer agent
trainer = Agent(
    role="Trainer",
    goal="Train users on AI tools and provide real-time feedback.",
    backstory="An expert trainer specializing in AI tools.",
    llm=llm
)
