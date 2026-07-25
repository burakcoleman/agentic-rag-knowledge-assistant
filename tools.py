import chromadb
from claude_agent_sdk import tool, create_sdk_mcp_server

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "course_materials"
TOP_K = 3

_client = chromadb.PersistentClient(path=CHROMA_DIR)
_collection = _client.get_or_create_collection(name=COLLECTION_NAME)


@tool(
    name="retrieve_documents",
    description=(
        "Search the course material knowledge base for passages relevant to a query. "
        "Use this whenever the user's question might be answered by the ingested course documents."
    ),
    input_schema={"query": str},
)
async def retrieve_documents(args):
    query = args["query"]
    results = _collection.query(query_texts=[query], n_results=TOP_K)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    if not documents:
        return {"content": [{"type": "text", "text": "No relevant documents found."}]}

    formatted = [
        f"[Source: {meta['source']}, page {meta['page']}, distance: {dist:.2f} (lower = closer match)]\n{doc}"
        for doc, meta, dist in zip(documents, metadatas, distances)
    ]
    return {"content": [{"type": "text", "text": "\n\n---\n\n".join(formatted)}]}


rag_server = create_sdk_mcp_server(
    name="rag",
    version="1.0.0",
    tools=[retrieve_documents],
)
