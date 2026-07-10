# Sentinel Platform

![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-green.svg)
![PyTorch](https://img.shields.io/badge/AI-PyTorch-orange.svg)
![Docker](https://img.shields.io/badge/deployment-Docker-blueviolet.svg)

## Project Overview

Sentinel is a robust, multi-tenant AI platform engineered for advanced analytics and forecasting. The platform's core is a high-performance FastAPI backend that provides a RESTful API for interacting with the system. It leverages LangGraph for sophisticated multi-agent orchestration, enabling complex, stateful AI workflows. The AI engine, built on PyTorch, delivers powerful time-series forecasting capabilities, forming the analytical backbone of the platform.

This repository contains the full source code, infrastructure definitions, and documentation for the Sentinel Platform.

## Repository Architecture

The Sentinel Platform is structured as a monorepo, with each directory representing a distinct microservice or component of the system. This design promotes modularity and independent development while maintaining a unified deployment strategy.

*   **`/backend/`**: Contains the primary FastAPI microservice. This service is responsible for handling all API requests, managing user tenants, and orchestrating AI tasks.
    *   **`/backend/agent/`**: Houses the core LangGraph implementation, including the state definitions, graph orchestration logic, and execution nodes.
*   **`/.github/`**: Contains CI/CD pipeline configurations and automated workflow definitions for the repository.

## Tech Stack

Our platform is built on modern, high-performance technologies chosen for their scalability and robust ecosystems.

### Backend

*   **Language**: Python 3.13
*   **Framework**: FastAPI
*   **Web Server**: Uvicorn
*   **AI Orchestration**: LangGraph
*   **Containerization**: Docker

### AI Engine

*   **Language**: Python 3.13
*   **Core Library**: PyTorch
*   **Environment**: Managed via Conda

## Getting Started

To get the backend service running locally for development or testing, you can use the provided Docker configuration.

**Prerequisites:**
*   Docker installed and running on your local machine.

**1. Build the Docker Image:**

Navigate to the `/backend` directory and run the build command.

```shell
cd backend
docker build -t sentinel-backend .
```

**2. Run the Docker Container:**

Once the image is built, you can start the container. This command maps port 8000 on your local machine to port 8000 in the container.

```shell
docker run -d -p 8000:8000 --name sentinel-backend-container sentinel-backend
```

The FastAPI backend will now be accessible at `http://localhost:8000`.