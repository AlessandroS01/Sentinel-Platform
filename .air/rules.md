# Project Sentinel: Senior Architectural AI Guidelines

## 1. Global Context & Architecture
- **Identity:** Sentinel is a production-grade, multi-tenant AI platform. 
- **Architecture:** It utilizes a Self-Hosted, Cloud-Native Architecture. 
- **Core AI:** The system integrates a dual AI architecture consisting of a PyTorch time-series forecasting model and a Multi-Agent RAG Orchestrator powered by LangGraph.
- **Deployment:** The platform is deployed across a containerized, 100% free Kubernetes infrastructure. 

## 2. Environment & OS Constraints
- **Target OS:** All generated Python code must be strictly compatible with a Linux deployment environment. 
- **File Routing:** You must use `pathlib` for all file system routing to ensure cross-platform compatibility. Never use hardcoded strings or Windows-specific file paths.
- **Containerization:** Assume all services run within isolated Docker containers orchestrated by Docker Compose or Kubernetes.

## 3. Agentic & AI Infrastructure Directives
- **Tool Calling:** Do not write hardcoded API wrappers for external data. The LangGraph agents act as Model Context Protocol (MCP) clients. 
- **MCP Servers:** Agents must seamlessly interface with dedicated, local MCP Servers to securely query external data boundaries. 
- **Custom Servers:** Use the mcp Python SDK (or FastMCP) to build the custom server for the live GDELT API.
- **Local LLMs:** The Synthesizer Agent rewrites summaries running locally via Ollama / Llama 3. 

## 4. Backend & Data Tooling Standards
- **API Framework:** Use FastAPI to serve asynchronous REST APIs and Server-Sent Events (SSE) for streaming LLM tokens.
- **Validation:** Pydantic must be used to enforce strict data validation for incoming requests, environment variable configuration, and LLM structured outputs.
- **Background Tasks:** Offload CPU-intensive tasks, such as API scraping and NER redaction, to Celery.
- **Databases:** Use PostgreSQL for relational data, MinIO for S3-compatible object storage, and Qdrant for the vector database. 
- **Caching:** Use Redis as an in-memory cache for JWT session token brokering, Celery message queuing, and strict API rate-limiting.

## 5. MLOps, CI/CD, & Observability
- **Experiment Tracking:** All PyTorch hyperparameters and LangChain experiment tracking metrics must be strictly tracked using MLflow.
- **Logging:** Standard printing is forbidden; use Loguru for formatted, structured JSON logs.
- **Metrics:** Prometheus scrapes the FastAPI metrics endpoint, and Grafana provides the visual dashboard.
- **CI/CD Debugging Protocol:** When GitHub Actions automated Ragas tests fail, pipeline debugging efforts are strictly designed to focus on fixing the test class rather than altering the core service logic itself.

## 6. Security & Guardrails
- **Data Isolation:** All database queries and PyTorch inferences are guarded by a user_id metadata filter.
- **Authentication:** Use JWT (JSON Web Tokens) for stateless, secure multi-tenant user sessions.
- **LLM Guardrails:** Pydantic schemas validate all outputs from the LangGraph agents before they are returned to the user. 
- **Redaction:** The Redactor Agent uses Named Entity Recognition (NER) to aggressively scrub polarizing names and inflammatory rhetoric from the text. Ensure this agent hasn't accidentally leaked the identities of protected sources.