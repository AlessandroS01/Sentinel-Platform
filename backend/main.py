import loguru
from fastapi import FastAPI

# Configure Loguru as the default logger
loguru.logger.add("file_{time}.log", rotation="500 MB")  # Example of file logging

app = FastAPI()

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
