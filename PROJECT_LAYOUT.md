# Project Structure Guide

## Directory Overview

```
Learningproject/
├── .adk/                    # ADK framework configuration
├── .venv/                   # Python virtual environment
├── .env                     # Environment variables (not pushed)
│
├── agents/                  # ADK Agent
│   ├── agent.py            # Main agent implementation
│   └── .adk/               # ADK config
│
├── mcp_server/             # MCP Server
│   ├── weather_mcp_server.py
│   └── .adk/               # ADK config
│
├── skills/                 # Skill definitions
│   └── weather_skill/
│       ├── SKILL.md
│       └── references/
│
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── .env.example           # Environment template
```

## Key Files

| File | Purpose |
|------|----------|
| agents/agent.py | ADK Agent with LiteLLM integration |
| mcp_server/weather_mcp_server.py | MCP server implementation |
| skills/weather_skill/SKILL.md | Skill definition |
| requirements.txt | Python packages |
| .env.example | Environment variable template |

## Development Setup

1. Install dependencies: pip install -r requirements.txt
2. Configure .env (copy from .env.example)
3. Start ADK Web: adk web
4. Visit http://localhost:3000

## Files Not Uploaded to GitHub

- .env (sensitive credentials)
- .venv/ (virtual environment)
- __pycache__/ (Python cache)
- statistics/ (local data)
- *.log (log files)

## Project Status

- ADK framework integration complete
- MCP server implemented with 3 tools
- Doubao model configured via LiteLLM
- Project ready for use and extension

Last Updated: 2026-04-03
