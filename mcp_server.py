from dotenv import load_dotenv
load_dotenv()
from mcp.server.fastmcp import FastMCP
from social import social_media_api
import os
mcp = FastMCP("social listening", json_response=True, stateless_http=True, port=3232)
GENESYS_DIVISON_ID = os.environ['GENESYS_DIVISON_ID']

@mcp.tool()
def create_topic(name: str):
    """Create a social listening topic in the system"""
    print(f"Creating topic: {name}")
    api_response = social_media_api.post_socialmedia_topics(body={"name": name, "divisionId": GENESYS_DIVISON_ID})
    print(api_response.to_json())
    return api_response



# Run with streamable HTTP transport
if __name__ == "__main__":
    print("running mcp")
    mcp.run(transport="streamable-http")