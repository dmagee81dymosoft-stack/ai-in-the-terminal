# Project Context - OpenCode

## Overview
OpenCode is an open-source AI tool that supports local models via Ollama.

## Project Details
- **Project:** AI Test Project
- **Tool:** OpenCode
- **Status:** Ready to configure
- **Created:** 2026-04-24

## Setup Requirements
```bash
# Install Ollama (if running local models)
# Visit: https://ollama.ai

# Supported Models
- Llama 2
- Mistral
- Neural Chat
- CodeLlama
```

## Quick Start
```bash
cd /workspaces/ai-in-the-terminal/ai-test-project
opencode  # Launch OpenCode
```

## Configuration
```json
{
  "model": "codellama",
  "temperature": 0.7,
  "contextWindow": 4096,
  "localOnly": true
}
```

## Key Advantages
- ✅ No API keys needed (local models)
- ✅ Complete privacy
- ✅ Offline capable
- ✅ Great for experimentation
- ✅ Free and open-source

## Context Persistence
This file maintains OpenCode session context.
Update with experiments, findings, and model preferences.

## Best Use Cases
- Privacy-focused development
- Local experimentation
- Building with open-source models
- Testing without API costs
- Learning LLM capabilities locally
