# Image MCP Generator

A minimal, production-ready Model Context Protocol (MCP) server designed to deliver random placeholder images. This project serves as a robust starting point for anyone looking to deploy their own MCP server, whether for local development, Docker, or cloud hosting.

## Features

- 🚀 **Quick Start**: Get up and running with a working MCP server in minutes.
- 🖼️ **Random Image API**: Instantly fetch random placeholder images with customizable sizes.
- 🐍 **Python SDK Example**: Demonstrates how to build and extend MCP servers using the Python SDK.
- 🐳 **Docker Support**: Easily build and run the server in a Docker container for production or testing.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yeoyujie/image-mcp-gen.git
   cd image-mcp-gen
   ```

2. **Set up environment variables:**

   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` as needed (default is `ENV=development`).

3. **Install dependencies:**

   ```bash
   uv sync
   ```

4. **Run the server locally (STDIO transport):**

   - With [MCP Inspector](https://github.com/modelcontextprotocol/inspector) (recommended for development):
     ```bash
     uv run mcp dev src/server.py
     ```
   - Or, run directly with Python (also uses STDIO transport, but without Inspector):
     ```bash
     uv run python src/server.py
     ```

5. **Run with Docker (Streamable HTTP transport):**

   - Build the Docker image:
     ```bash
     docker build -t image-mcp-gen .
     ```
   - Run the container:
     ```bash
     docker run -p 8000:8000 image-mcp-gen
     ```

6. **Connect and test the MCP server:**

   - You can use the provided `.vscode/mcp.json` to connect to this MCP server with GitHub Copilot. For Claude Desktop or other MCP clients, please refer to their documentation for connection or configuration instructions.
   - After connecting, try asking:

     > Generate a random image of width 300

## Why image-mcp-gen?

- **Educational**: Learn how to implement and deploy MCP servers with clear, well-documented code.
- **Template**: Use as a boilerplate for your own MCP-based projects.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License.
