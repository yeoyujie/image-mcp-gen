# Image MCP Generator

A minimal, production-ready Model Context Protocol (MCP) server designed to deliver random placeholder images. This project serves as a robust starting point for anyone looking to deploy their own MCP server, whether for local development or cloud hosting.

## Features

- 🚀 **Quick Start**: Get up and running with a working MCP server in minutes.
- 🖼️ **Random Image API**: Instantly fetch random placeholder images with customizable sizes.
- 🐍 **Python SDK Example**: Demonstrates how to build and extend MCP servers using the Python SDK.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yeoyujie/image-mcp-gen.git
   cd image-mcp-gen
   ```

2. **Install dependencies:**

   ```bash
   uv sync
   ```

3. **Run the server (with [MCP Inspector](https://github.com/modelcontextprotocol/inspector)):**

   ```bash
   uv run mcp dev src/server.py
   ```

4. **Fetch a random image:**
   - Use the provided API endpoint to get a random image of any size, e.g.:
     `GET /random-image?width=200&height=300`

## Why image-mcp-gen?

- **Educational**: Learn how to implement and deploy MCP servers with clear, well-documented code.
- **Template**: Use as a boilerplate for your own MCP-based projects.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License.
