from typing import TypedDict, List

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        query: The user's query.
        retrieved_context: A list of retrieved context.
        redacted_content: The redacted content.
        final_brief: The final brief.
    """
    query: str
    retrieved_context: List[str]
    redacted_content: str
    final_brief: str
