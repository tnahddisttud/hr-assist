## **HR-ASSIST Agentic AI System**
---
HR ASSIST is an Agentic AI system designed to help HR teams automate routine workflows. This example demonstrates automation of the employee onboarding process, streamlining tasks that typically require manual intervention.

In terms of technical architecture, for MCP client we use Claude Desktop and the code base here represents the MCP server with necessary tools that will be used by MCP client 

🛠️ Setup Instructions

To set up and run HR ASSIST, follow these steps:

- Configure claude_desktop_config.json
Add the following configuration to your claude_desktop_config.json file:

    ```json
    {
    "mcpServers": {
        "hr-assist": {
        "command": "C:\\Users\\dhaval\\.local\\bin\\uv",
        "args": [
            "--directory",
            "C::\\code\\atliq-hr-assist",
            "run",
            "server.py"
        ]
        }
    }
    }
    ```

- Run `uv init` and `uv add mcp[cli]` as per the video tutorial in the course.

## Testing with MCP Inspector

You can test the MCP server interactively without Claude Desktop using the MCP Inspector. Run the following command in your terminal:

```bash
npx @modelcontextprotocol/inspector uv run server.py
```


All rights reserver @Codebasics Inc and LearnerX India Private Ltd.