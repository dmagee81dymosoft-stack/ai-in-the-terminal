# Getting Started with AI Tools

## Installed & Ready

### ✅ Gemini CLI
**Status:** Installed v0.39.1 and ready to use  
**Cost:** Free (generous tier)  
**Launch:** `gemini`  
**Best for:** Quick tasks, web research, creative writing

### ⏳ Claude Code
**Status:** Available (requires setup + Claude Pro subscription)  
**Cost:** Claude Pro ($20/mo)  
**Launch:** `claude3` or similar  
**Best for:** Complex coding, architecture, refactoring

### ⏳ OpenCode
**Status:** Available (requires setup + optional Ollama)  
**Cost:** Free (with local models)  
**Launch:** `opencode`  
**Best for:** Privacy, experimentation, local models

### ⏳ Codex
**Status:** Available (requires ChatGPT Plus)  
**Cost:** ChatGPT Plus ($20/mo)  
**Launch:** `codex`  
**Best for:** Code analysis, learning

## Your First Steps

### Step 1: Launch Gemini CLI
```bash
cd /workspaces/ai-in-the-terminal/ai-test-project
gemini
```

### Step 2: Try a Simple Task
```
> Write a Python script that prints "Hello, AI!"
```

### Step 3: Create a File
```
> Create a file called app.py with a Flask web server
```

Type `y` when asked to create the file.

### Step 4: Update Context
Inside Gemini CLI, type:
```
> /init
```

This updates `gemini.md` with your project context.

### Step 5: Exit and Reopen
```
> exit
```

Reopen Gemini CLI:
```bash
gemini
```

Notice how it remembers your project? That's the power of context files!

## Multi-Tool Workflow

Once you're comfortable with Gemini, you can:
1. Use Gemini for quick ideas and research
2. Use Claude Code for serious development (if subscribed)
3. Use OpenCode for private experimentation
4. Sync context across all tools

See [Multi-Tool Workflow](../../docs/08-multi-tool-workflow.md) for details.

## Directory Guide

| Directory | Purpose |
|-----------|---------|
| `src/` | Your generated code files |
| `docs/` | Notes, research, documentation |
| `config/` | Tool configurations and settings |
| `gemini.md` | Context file for Gemini CLI (auto-updated) |
| `claude.md` | Context file for Claude Code |
| `opencode.md` | Context file for OpenCode |

## Key Files

- **gemini.md** - Gemini CLI context (main)
- **README.md** - Project overview
- **config/gemini-config.json** - Tool configuration
- **.gitignore** - Git settings

## Tips & Tricks

1. **Update Context Regularly**: Run `/init` in tools to refresh context
2. **Keep Notes**: Document what you learn in /docs
3. **Save Outputs**: Let AI create files directly in /src
4. **Read Logs**: Check terminal output for insights
5. **Use Web Search**: Gemini can search for current info

## Troubleshooting

**Gemini won't launch?**
```bash
# Check installation
which gemini

# Reinstall if needed
npm install -g @google/gemini-cli
```

**Permission errors?**
```bash
# Try with sudo
sudo gemini
```

**Can't create files?**
Ensure the project directory is writable:
```bash
ls -la /workspaces/ai-in-the-terminal/ai-test-project
```

## Next Resources

- [Gemini CLI Full Guide](../../docs/03-gemini-cli.md)
- [Claude Code Guide](../../docs/04-claude-code.md)
- [OpenCode Guide](../../docs/06-opencode.md)
- [Command Cheat Sheet](../../docs/14-cheat-sheet.md)

---

**Ready? Launch Gemini:**
```bash
gemini
```
