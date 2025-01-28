from crewai.tools import BaseTool
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)

class SuggestAIToolTool(BaseTool):
    name: str = "suggest_ai_tool"
    description: str = "Suggests AI tools based on a given job workflow."

    def _run(self, question: str, answer: str):
        """
        Use the LLM to analyze the workflow and suggest AI tools.
        """
        if not question or not answer:
            raise ValueError("Both 'question' and 'answer' are required.")
        prompt = f"{question}\n\nWorkflow Description:\n{answer}"
        response = llm.invoke([{"role": "system", "content": prompt}])
        return response.content.strip().split("\n")
