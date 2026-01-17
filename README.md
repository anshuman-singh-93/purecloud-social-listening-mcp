# MCP PureCloud Social Listening

This project implements a Model Context Protocol (MCP) server that integrates with Genesys Cloud (PureCloud) to provide social listening capabilities to AI agents. It includes a web interface to interact with the agent.

## Overview

The system allows an AI agent to perform actions within Genesys Cloud, specifically focused on Social Listening. Currently, it supports creating social listening topics. The architecture consists of:

-   **MCP Server (`mcp_server.py`)**: Exposes Genesys Cloud functionality as tools using the Model Context Protocol.
-   **Genesys Cloud Client (`social.py`)**: Handles authentication and API calls to PureCloud.
-   **Agent (`agent.py`)**: An intelligent agent (using `openai-agents`) that utilizes the MCP tools to fulfill user requests.
-   **Web App (`app.py`)**: A FastAPI-based frontend for users to interact with the agent.

## Prerequisites

-   Python 3.14 or higher
-   A Genesys Cloud (PureCloud) account with appropriate permissions.
-   OAuth Client Credentials (Client ID and Secret) for Genesys Cloud.

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
    pip install -r requirements.txt # (If you generate one)
    ```

## Configuration

Create a `.env` file in the root directory with the following environment variables:

```env
GENESYS_CLOUD_CLIENT_ID=your_client_id
GENESYS_CLOUD_CLIENT_SECRET=your_client_secret
GENESYS_CLOUD_ENVIRONMENT=mypurecloud.com  # e.g., mypurecloud.com, usw2.pure.cloud
GENESYS_DIVISON_ID=your_division_id
```

## Usage

You need to run both the MCP server and the Web Application.

### 1. Start the MCP Server

The MCP server provides the tools to the agent.

```bash
python mcp_server.py
```
This will start the MCP server on port 3232.

### 2. Start the Web Application

The web application hosts the chat interface.

```bash
python app.py
```
Or using uvicorn directly:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### 3. Interact

Open your browser and navigate to `http://localhost:8000`. You can now chat with the agent. For example, you can ask:

> "Create a social listening topic named 'Competitor Analysis'"

## File Structure

-   `mcp_server.py`: The MCP server implementation defining tools like `create_topic`.
-   `social.py`: Genesys Cloud API client initialization and authentication.
-   `agent.py`: Agent logic using `openai-agents` to connect to the MCP server.
-   `app.py`: FastAPI web server serving the frontend and handling user requests.
-   `pyproject.toml`: Project dependencies and metadata.

## Tools

Currently available tools:

-   **`create_topic(name: str)`**: Creates a new social listening topic in the configured Genesys Cloud division.
