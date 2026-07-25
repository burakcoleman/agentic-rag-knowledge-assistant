import gradio as gr
from dotenv import load_dotenv
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock
from tools import rag_server
from main import SYSTEM_PROMPT

load_dotenv()

options = ClaudeAgentOptions(
    system_prompt=SYSTEM_PROMPT,
    setting_sources=[],
    strict_mcp_config=True,
    mcp_servers={"rag": rag_server},
    allowed_tools=["mcp__rag__retrieve_documents"],
)

_client = None


async def respond(message, history):
    global _client
    if _client is None:
        _client = ClaudeSDKClient(options=options)
        await _client.connect()

    await _client.query(message)

    response_text = ""
    async for msg in _client.receive_response():
        if isinstance(msg, AssistantMessage):
            for block in msg.content:
                if isinstance(block, TextBlock):
                    response_text += block.text
                    yield response_text


demo = gr.ChatInterface(
    fn=respond,
    title="Course Assistant",
    description="Ask questions about the ingested course materials.",
    theme=gr.themes.Soft(),
    css=".gradio-container { max-width: 720px !important; margin: auto !important; }",
)

if __name__ == "__main__":
    demo.launch()
