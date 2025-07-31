import requests
from io import BytesIO
from PIL import Image as PILImage
from mcp.server.fastmcp import FastMCP, Image, Context

mcp = FastMCP("Random Image Generator MCP", port=8000, host="0.0.0.0")
base_url = "https://picsum.photos"


@mcp.tool()
async def get_random_image(
    width: int = 200,
    height: int = 300,
    id: int = None,
    seed: str = None,
    grayscale: bool = False,
    blur: int = None,
    ctx: Context = None
) -> Image:
    """
    Return a random or customized image from https://picsum.photos/ with the given options.
    
    Args:
        width (int): Image width.
        height (int): Image height.
        id (int, optional): Specific image ID.
        seed (str, optional): Seed for static random image.
        grayscale (bool): Return grayscale image if True.
        blur (int, optional): Blur amount (1-10).
    """
    path = ""
    if id is not None:
        path = f"/id/{id}/{width}/{height}"
    elif seed is not None:
        path = f"/seed/{seed}/{width}/{height}"
    else:
        path = f"/{width}/{height}"
    params = []
    if grayscale:
        params.append("grayscale")
    if blur is not None:
        if 1 <= blur <= 10:
            params.append(f"blur={blur}")
        else:
            params.append("blur")
    query = ""
    if params:
        query = "?" + "&".join(params)
    url = f"{base_url}{path}{query}"
    await ctx.info(f"Calling URL: {url}")
    response = requests.get(url)
    img = PILImage.open(BytesIO(response.content))
    output = BytesIO()
    img.save(output, format="PNG")
    return Image(data=output.getvalue(), format="png")

def main():
    mcp.run(transport="streamable-http")
    # mcp.run()

if __name__ == "__main__":
    main()