import asyncio
from dotenv import load_dotenv
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
    ToolUseBlock,
    ResultMessage,
)
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

RETRIEVAL_TOOL_NAME = "mcp__rag__retrieve_documents"

TEST_CASES = [
    {
        "question": "What elements does the syllabus checklist require?",
        "expects_retrieval": True,
        "check_keywords": ["Course Title", "Student Learning Outcomes"],
    },
    {
        "question": "What technology do law students need to bring to class?",
        "expects_retrieval": True,
        "check_keywords": ["laptop"],
    },
    {
        "question": "What should instructors tell students about reporting sexual harassment?",
        "expects_retrieval": True,
        "check_keywords": ["Title IX"],
    },
    {
        "question": "What is the late-assignment penalty policy?",
        "expects_retrieval": True,
        "check_keywords": [],
    },
    {
        "question": "What is the capital of France?",
        "expects_retrieval": False,
        "check_keywords": ["Paris"],
    },
    {
        "question": "Write a haiku about autumn.",
        "expects_retrieval": False,
        "check_keywords": [],
    },
]


async def run_case(case):
    async with ClaudeSDKClient(options=options) as client:
        await client.query(case["question"])

        answer_text = ""
        retrieval_count = 0
        cost_usd = None
        duration_ms = None

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        answer_text += block.text
                    elif isinstance(block, ToolUseBlock) and block.name == RETRIEVAL_TOOL_NAME:
                        retrieval_count += 1
            elif isinstance(message, ResultMessage):
                cost_usd = message.total_cost_usd
                duration_ms = message.duration_ms

    retrieval_called = retrieval_count > 0
    retrieval_ok = retrieval_called == case["expects_retrieval"]
    keywords_ok = all(kw.lower() in answer_text.lower() for kw in case["check_keywords"])
    passed = retrieval_ok and keywords_ok

    return {
        "question": case["question"],
        "expects_retrieval": case["expects_retrieval"],
        "retrieval_called": retrieval_called,
        "retrieval_count": retrieval_count,
        "keywords_ok": keywords_ok,
        "passed": passed,
        "answer": answer_text,
        "cost_usd": cost_usd,
        "duration_ms": duration_ms,
    }


def fmt_cost(cost_usd):
    return f"${cost_usd:.4f}" if cost_usd is not None else "N/A"


def fmt_ms(duration_ms):
    return f"{duration_ms}" if duration_ms is not None else "N/A"


async def main():
    results = [await run_case(case) for case in TEST_CASES]

    lines = [
        "# Evaluation Results",
        "",
        "| # | Question | Retrieval (expected/actual) | Keywords OK | Pass | Cost | Latency (ms) |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(results, 1):
        lines.append(
            f"| {i} | {r['question']} | {r['expects_retrieval']}/{r['retrieval_called']} "
            f"(x{r['retrieval_count']}) | {r['keywords_ok']} | {'PASS' if r['passed'] else 'FAIL'} | "
            f"{fmt_cost(r['cost_usd'])} | {fmt_ms(r['duration_ms'])} |"
        )

    total_cost = sum(r["cost_usd"] or 0 for r in results)
    known_latencies = [r["duration_ms"] for r in results if r["duration_ms"] is not None]
    avg_latency = sum(known_latencies) / len(known_latencies) if known_latencies else 0
    pass_count = sum(1 for r in results if r["passed"])

    lines += [
        "",
        f"**Summary:** {pass_count}/{len(results)} passed, "
        f"total cost {fmt_cost(total_cost)}, average latency {avg_latency:.0f} ms.",
        "",
        "## Full answers",
        "",
        "Read these manually too -- the keyword checks above are a shortcut, not proof of correctness "
        "(e.g. case 4 has no keyword check since it tests whether the agent honestly says the "
        "syllabus doesn't specify a late-assignment policy, instead of guessing).",
        "",
    ]
    for i, r in enumerate(results, 1):
        lines.append(f"**{i}. {r['question']}**\n\n{r['answer']}\n")

    report = "\n".join(lines)
    with open("EVALUATION.md", "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    asyncio.run(main())
