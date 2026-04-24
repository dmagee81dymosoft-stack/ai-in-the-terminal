# AI-Driven Containerized Workflow

This document describes how to use Gemini CLI and Docker to manage your development lifecycle.

## 🚀 Getting Started

### 1. Build and Run the Container
Use Docker Compose to start your application in development mode:
```bash
docker compose up -d --build
```

### 2. Verify the Service
Check if the service is running:
```bash
curl http://localhost:5001
```

### 3. Use Gemini CLI for Tasks
You can use Gemini CLI to perform tasks inside or related to the container:

**Example: Generate a new API endpoint**
> "Add a /health endpoint to app.py that returns the system status"

**Example: Fix a bug**
> "The container is crashing with a ModuleNotFoundError. Check my requirements.txt and Dockerfile"

## 🛠 Management CLI Commands

| Action | Command |
|--------|---------|
| Start | `docker compose up -d` |
| Stop | `docker compose down` |
| Logs | `docker compose logs -f` |
| Shell | `docker compose exec web bash` |
| Rebuild | `docker compose up -d --build` |

## 🧠 AI Integration
This workflow is designed to be "Context-Aware". When you run `/init`, Gemini CLI will see your `docker-compose.yml` and `Dockerfile`, allowing it to:
1. Suggest optimizations for your images.
2. Debug environment variable issues.
3. Help scale your services by adding new components to the compose file.

## 🌐 Connectivity
Since Tailscale is active on this machine, you can access this container from any device on your tailnet using:
`http://100.64.133.97:5001`
