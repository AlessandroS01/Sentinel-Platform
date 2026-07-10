from typing import TypedDict, List


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        query: The incoming user claim.
        raw_context: Unredacted context text retrieved.
        redacted_context: Text stripped of identifying data.
        final_brief: The final anonymous intelligence summary.
    """

    query: str
    raw_context: List[str]
    redacted_context: str
    final_brief: str
