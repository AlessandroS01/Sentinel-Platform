from langgraph.graph import StateGraph, END

from agent.nodes import retrieve_node, redact_node, synthesize_node
from agent.state import GraphState

# Initialize the graph
workflow = StateGraph(GraphState)

# Add the nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("redact", redact_node)
workflow.add_node("synthesize", synthesize_node)

# Set the entry point
workflow.set_entry_point("retrieve")

# Add the edges
workflow.add_edge("retrieve", "redact")
workflow.add_edge("redact", "synthesize")
workflow.add_edge("synthesize", END)

# Compile the graph
app = workflow.compile()
