from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
from loguru import logger

from agent.state import GraphState

# Initialize the Ollama LLM
llm = ChatOllama(model="gemma4:latest", temperature=0.1)


async def retrieve_node(state: GraphState) -> dict:
    """
    Simulate retrieving highly polarized, entity-dense OSINT/fact-checking text.
    """
    logger.info("---RETRIEVING CONTEXT---")
    query = state["query"]
    # Simulate retrieval of polarized text
    raw_context = [
        f"Regarding '{query}': A report by the Liberty Sentinel claims widespread election fraud, citing anonymous sources within the Williamson Campaign.",
        f"FactCheck.org, however, rates claims of fraud in the '{query}' case as 'unsubstantiated,' noting a lack of concrete evidence from official sources.",
        "On the social media network TruthWeaver, user @PatriotPete22 posted a video showing alleged ballot tampering by activists affiliated with the Justice Now party.",
    ]
    logger.info(f"Raw context retrieved for query: '{query}'")
    return {"raw_context": raw_context}


async def redact_node(state: GraphState) -> dict:
    """
    Acts as a compliance officer, scrubbing identifying data from the context.
    """
    logger.info("---REDACTING CONTEXT---")
    raw_context = "\n\n".join(state["raw_context"])

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a compliance officer. Your task is to aggressively scrub all names, parties, networks, and inflammatory rhetoric from the following text, replacing them with `[REDACTED]`. Preserve the core information but remove all identifying or emotionally charged language.",
            ),
            ("user", "Text to redact:\n\n{context}"),
        ]
    )
    chain = prompt | llm | StrOutputParser()
    redacted_context = await chain.ainvoke({"context": raw_context})
    logger.info("Context has been redacted.")
    return {"redacted_context": redacted_context}


async def synthesize_node(state: GraphState) -> dict:
    """
    Acts as an executive editor, creating a sharp, anonymous intelligence summary.
    """
    logger.info("---SYNTHESIZING FINAL BRIEF---")
    redacted_context = state["redacted_context"]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an executive editor. Your task is to transform the following redacted"
                " text into a sharp, anonymous 3-bullet-point intelligence summary. Focus on the"
                " factual claims and counter-claims, ignoring the redacted emotional language.",
            ),
            ("user", "Redacted text:\n\n{context}"),
        ]
    )
    chain = prompt | llm | StrOutputParser()
    final_brief = await chain.ainvoke({"context": redacted_context})
    logger.info("Final brief synthesized.")
    return {"final_brief": final_brief}
