# Project Context - Gemini CLI

## Project Overview
**Name:** AI Test Project  
**Purpose:** Learning and testing terminal AI workflows  
**Created:** 2026-04-24  

## Project Structure
```
ai-test-project/
├── src/           # Source code
│   └── app.py     # Flask Application
├── docs/          # Documentation
│   ├── GETTING-STARTED.md
│   └── WORKFLOW.md
├── config/        # Configuration files
│   └── gemini-config.json
├── Dockerfile     # Container definition
├── docker-compose.yml # Orchestration
├── requirements.txt   # Python dependencies
└── README.md      # Project documentation
```

## Current Status
- **Context Updated:** 2026-04-24
- **Environment:** Gemini CLI v0.39.1
- **Status:** CLI & Containerized Workflow configured.
- **Connectivity:** Tailscale Active (100.64.133.97)

## Infrastructure & Connectivity
- **Tailscale:** Installed (v1.96.4)
- **Hostname:** `gemini-cli-test`
- **Docker:** Plugins configured (Scout, Extension CLI, Buildx, Compose).
- **App Service:** Accessible at port 5001.

## Key Notes
- This is a test/learning project.
- Use Gemini CLI for all AI tasks.
- Containerized development is the primary workflow.

## Gemini CLI Commands Reference
- `gemini` - Launch interactive mode
- `/init` - Initialize/update context file
- `/exit` - Exit Gemini CLI

## Next Steps
1. Run `docker compose up -d` to start the application.
2. Test connectivity via `curl http://localhost:5001`.
3. Use Gemini to add features to `app.py`.
