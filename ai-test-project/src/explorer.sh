#!/bin/bash

# Explorer AI - Project Analysis Script
echo "🔍 Explorer AI: Analyzing project status..."

# 1. Project Structure Analysis
echo "--- Structure ---"
tree -L 2 --noreport

# 2. Connectivity Check
echo "--- Connectivity ---"
if command -v tailscale >/dev/null; then
    sudo tailscale --socket=/run/tailscale/tailscaled.sock status | head -n 1
else
    echo "Tailscale not found."
fi

# 3. Docker Status
echo "--- Docker Services ---"
docker compose ps

# 4. AI Insights (Using Gemini CLI)
echo "--- AI Insights ---"
gemini "Analyze the current project structure and status based on these files: $(ls -m). Suggest one next step for development."
