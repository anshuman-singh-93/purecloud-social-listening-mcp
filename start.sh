#!/bin/bash

# Start the MCP Server in the background
python mcp_server.py &

# Start the Web Application in the foreground
uvicorn app:app --host 0.0.0.0 --port 8000
