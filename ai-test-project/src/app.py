from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "AI-Integrated Containerized Workflow Active",
        "environment": os.getenv("APP_ENV", "development"),
        "hostname": os.getenv("HOSTNAME", "unknown")
    })

@app.route('/ai-task')
def task():
    # Placeholder for AI processing logic
    return jsonify({
        "task": "Process Data",
        "result": "Success",
        "agent": "Gemini CLI"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "container": os.getenv("HOSTNAME", "unknown"),
        "environment": os.getenv("APP_ENV", "development")
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    # Enable debug mode for hot-reloading
    app.run(host='0.0.0.0', port=port, debug=True)
