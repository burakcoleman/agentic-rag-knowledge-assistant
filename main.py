import asyncio
from dotenv import load_dotenv
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock
from tools import rag_server

load_dotenv()

SYSTEM_PROMPT = """You are a course assistant that answers student questions using the ingested course materials.

- Use the retrieve_documents tool whenever the question might be answered by the course materials.
- Base your answer only on what the retrieved passages say. If they don't contain the answer, say so honestly instead of guessing.
- Always cite your sources at the end of your answer, in the format (Source: filename, page N).
"""


async def main():
    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        setting_sources=[],
        strict_mcp_config=True,
        mcp_servers={"rag": rag_server},
        allowed_tools=["mcp__rag__retrieve_documents"],
    )

    print("Course Assistant -- type 'exit' to quit.\n")

    async with ClaudeSDKClient(options=options) as client:
        while True:
            user_input = input("You: ").strip()
            if not user_input or user_input.lower() in ("exit", "quit"):
                break

            await client.query(user_input)
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"Assistant: {block.text}")


if __name__ == "__main__":
    asyncio.run(main())
