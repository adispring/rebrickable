from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

llm = ChatOpenAI(
    model="gpt-4o-2024-11-20",
    base_url=os.getenv("OPENAI_ENDPOINT"),
    api_key=os.getenv("OPENAI_API_KEY")
)

async def main():
    agent = Agent(
        task="Compare the price of gpt-4-turbo-preview and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())