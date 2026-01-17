# MCP Server with FastAPI and OpenAI - Implementation Steps

## What We Built

A complete MCP (Model Context Protocol) server that:
- Implements MCP protocol with custom tools
- Provides FastAPI REST API endpoints
- Integrates with OpenAI's GPT models for AI-powered responses
- Supports both HTTP and stdio modes
- Includes tool calling/function calling capabilities

## Project Structure

```
.
├── main.py                    # Main server implementation
├── test_server.py            # Automated test suite
├── example_client.py         # Example usage client
├── README.md                 # Full documentation
├── QUICKSTART.md            # Quick start guide
├── mcp-config-example.json  # MCP configuration example
├── .env.example             # Environment variables template
├── pyproject.toml           # Python dependencies
└── uv.lock                  # Locked dependencies
```

## Key Features Implemented

### 1. MCP Server
- Tool registration and listing
- Tool execution handlers
- Stdio server mode for MCP clients

### 2. FastAPI Integration
- Health check endpoint (`GET /`)
- Tools listing endpoint (`GET /tools`)
- Chat endpoint with OpenAI (`POST /chat`)
- Direct tool execution (`POST /tool/{tool_name}`)

### 3. OpenAI Integration
- Async OpenAI client
- Function calling support
- Tool result processing
- Multi-turn conversations

### 4. Built-in Tools
- `get_weather`: Get weather for a location (simulated)
- `calculate`: Perform mathematical calculations

## How to Use

### As FastAPI Server
```bash
python main.py
# Server runs at http://localhost:8000
```

### As MCP Stdio Server
```bash
python main.py mcp
# Runs in stdio mode for MCP clients
```

### Testing
```bash
# Run automated tests
python test_server.py

# Run example client
python example_client.py
```

## API Examples

### Chat with AI
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is 25 * 4?",
    "api_key": "your-openai-key"
  }'
```

### Execute Tool Directly
```bash
curl -X POST http://localhost:8000/tool/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression": "25 * 4"}'
```

## Dependencies

- `mcp>=1.1.2` - Model Context Protocol SDK
- `fastapi>=0.115.0` - Web framework
- `openai>=1.59.5` - OpenAI API client
- `uvicorn>=0.32.0` - ASGI server
- `httpx>=0.28.1` - HTTP client
- `pydantic>=2.10.4` - Data validation

## Architecture

```
┌─────────────────┐
│   MCP Client    │
│   (Kiro, etc)   │
└────────┬────────┘
         │ stdio
         ▼
┌─────────────────┐     ┌──────────────┐
│   MCP Server    │────▶│  OpenAI API  │
│   (main.py)     │     │   (GPT-4)    │
└────────┬────────┘     └──────────────┘
         │ HTTP
         ▼
┌─────────────────┐
│  FastAPI REST   │
│   Endpoints     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  HTTP Clients   │
│  (curl, etc)    │
└─────────────────┘
```

## Next Steps

1. Add more tools (database queries, API calls, etc.)
2. Implement authentication/authorization
3. Add request logging and monitoring
4. Create a web UI for testing
5. Add more sophisticated error handling
6. Implement rate limiting
7. Add tool result caching

## Notes

- The server supports dual mode: HTTP (FastAPI) and stdio (MCP)
- OpenAI API key can be set via environment variable or per-request
- Tools are automatically available to both MCP clients and HTTP endpoints
- Uses latest MCP SDK (1.1.2+) and OpenAI SDK (1.59.5+)
