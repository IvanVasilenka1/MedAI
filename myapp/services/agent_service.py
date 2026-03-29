from __future__ import annotations
import asyncio

from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import create_agent

from myapp.prompts.system import system_prompt
from myapp.prompts.tool import tool_description
from myapp.tools.qdrant import QdrantToolClass
from myapp.utils.config import  config
from myapp.utils.embeddings import OllamaEmbeddings


class MedicalAgent:
    def __init__(
        self
    ):
        self.embedding_client = OllamaEmbeddings(model="mxbai-embed-large")
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=config.openai_api_key,
            temperature=0.5
        )

        self.qdrant_tool = QdrantToolClass(self.embedding_client)



        self.tools = [
            Tool(
                name="qdrant_search",
                func=lambda x: asyncio.run(self.qdrant_tool.run(x)),
                description=tool_description
            ),
        ]

        self.agent = create_agent(
            model=self.llm,
            tools=self.tools
        )

    def run(self, user_text: str) -> str:
        result = self.agent.invoke({
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ]
        })

        return result["messages"][-1].content