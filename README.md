# MCP PureCloud Social Listening

This project implements a Model Context Protocol (MCP) server that integrates with Genesys Cloud (PureCloud) to provide social listening capabilities to AI agents. It includes a web interface to interact with the agent.

## Overview

The system allows an AI agent to perform actions within Genesys Cloud, specifically focused on Social Listening. Currently, it supports creating social listening topics. The architecture consists of:

-   **MCP Server (`mcp_server.py`)**: Exposes Genesys Cloud functionality as tools using the Model Context Protocol.
-   **Genesys Cloud Client (`social.py`)**: Handles authentication and API calls to PureCloud.
-   **Agent (`agent.py`)**: An intelligent agent (using `openai-agents`) that utilizes the MCP tools to fulfill user requests.
-   **Web App (`app.py`)**: A FastAPI-based frontend for users to interact with the agent.

## Prerequisites

-   Python 3.12 or higher
-   A Genesys Cloud (PureCloud) account with appropriate permissions.
-   OAuth Client Credentials (Client ID and Secret) for Genesys Cloud.
-   OpenAI API Key (for the agent).

## Installation

This project uses `uv` for dependency management.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mcp-purecloud-social-listening
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    # Or using pip
    pip install .
    ```

## Configuration

Create a `.env` file in the root directory with the following environment variables:

```env
GENESYS_CLOUD_CLIENT_ID=your_client_id
GENESYS_CLOUD_CLIENT_SECRET=your_client_secret
GENESYS_CLOUD_ENVIRONMENT=mypurecloud.com  # e.g., mypurecloud.com, usw2.pure.cloud
GENESYS_DIVISON_ID=your_division_id
API_MAGIC_TOKEN=random token to protect api
OPENAI_API_KEY=your_openai_api_key
```

## Usage

You can run the application directly or using Docker.

### Option 1: Docker (Recommended)

Build and run the container. This handles both the server and the web app in one go.

```bash
docker build -t mcp-social-listening .
docker run -p 8000:8000 --env-file .env mcp-social-listening
```

Then visit `http://localhost:8000`.

### Option 2: Local Development

You need to run both the MCP server and the Web Application. We provided a helper script:

```bash
./start.sh
```

Or run them manually in separate terminals:

1.  **Start the MCP Server** (Port 3232)
    ```bash
    python mcp_server.py
    ```

2.  **Start the Web Application** (Port 8000)
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

### Interact

Open your browser and navigate to `http://localhost:8000`. You can now chat with the agent. For example, you can ask:

> "Create a social listening topic named 'Competitor Analysis'"

## File Structure

-   `mcp_server.py`: The MCP server implementation defining tools like `create_topic`.
-   `social.py`: Genesys Cloud API client initialization and authentication.
-   `agent.py`: Agent logic using `openai-agents` to connect to the MCP server.
-   `app.py`: FastAPI web server serving the frontend and handling user requests.
-   `pyproject.toml`: Project dependencies and metadata.
-   `Dockerfile`: Configuration for containerizing the application.
-   `start.sh`: Startup script for running services.

## Tools

Currently available tools:

-   **`create_topic(name: str)`**: Creates a new social listening topic in the configured Genesys Cloud division.

## Deployment

The simplest way to host this application is using the provided `Dockerfile`. This allows you to deploy to any platform that supports Docker (e.g., Railway, Render, Fly.io, DigitalOcean).

### 1. Railway / Render (Recommended)

1.  Push this repository to GitHub.
2.  Connect your GitHub repository to Railway or Render.
3.  It will automatically detect the `Dockerfile`.
4.  **Important**: You must set all the Environment Variables in the hosting dashboard (Railway/Render console), including `OPENAI_API_KEY`.

### 2. Manual Docker Run

You can build and run the container locally or on a VPS:

```bash
docker build -t mcp-social-listening .
docker run -p 8000:8000 \
  -e GENESYS_CLOUD_CLIENT_ID=... \
  -e GENESYS_CLOUD_CLIENT_SECRET=... \
  -e GENESYS_CLOUD_ENVIRONMENT=... \
  -e GENESYS_DIVISON_ID=... \
  -e API_MAGIC_TOKEN=... \
  -e OPENAI_API_KEY=... \
  mcp-social-listening
```

