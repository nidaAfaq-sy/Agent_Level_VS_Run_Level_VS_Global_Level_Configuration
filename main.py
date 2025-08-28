from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.run import RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",   
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

English_teacher = Agent(
    name="English Teacher",
    instructions="You are a helpful assistant that can help with English grammar and vocabulary",
)

async def main():
    runner = Runner()
    result = await runner.run(
        English_teacher,
        "how many tenses in grammar?",
        run_config=config
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

