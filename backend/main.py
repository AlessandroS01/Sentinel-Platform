import loguru
from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import app as langgraph_app

# Configure Loguru as the default logger
loguru.logger.add("file_{time}.log", rotation="500 MB")  # Example of file logging

app = FastAPI()

class PitchRequest(BaseModel):
    query: str

@app.on_event("startup")
async def startup_event():
    loguru.logger.info("Application starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    loguru.logger.info("Application shutting down...")

@app.get("/health")
async def health():
    """
    Health check endpoint to ensure the service is running.
    """
    loguru.logger.info("Health check endpoint was called.")
    return {"status": "ok"}

@app.post("/pitch")
async def pitch(request: PitchRequest):
    """
    Endpoint to process a query and return a pitch.
    """
    loguru.logger.info(f"Received pitch request for query: {request.query}")
    result = await langgraph_app.ainvoke({"query": request.query})
    loguru.logger.info("Pitch request processed successfully.")
    return result
