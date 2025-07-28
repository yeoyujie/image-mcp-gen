import requests
from io import BytesIO
from PIL import Image as PILImage
from mcp.server.fastmcp import FastMCP, Image

mcp = FastMCP("Random Image Generator MCP", port=8000, host="localhost")


@mcp.tool()
def get_random_image(width: int = 200, height: int = 300) -> Image:
    """Return a random image from https://picsum.photos/ with the given width and height."""
    url = f"https://picsum.photos/{width}/{height}"
    response = requests.get(url)
    img = PILImage.open(BytesIO(response.content))
    output = BytesIO()
    img.save(output, format="PNG")
    return Image(data=output.getvalue(), format="png")

def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()