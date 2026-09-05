import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command=".venv\\Scripts\\python.exe",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            resources = await session.list_resources()

            print("Available MCP resources:")

            for resource in resources.resources:
                print(f"- {resource.uri}")

            result = await session.read_resource(
                "customers://all"
            )

            print("\nResource data:")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())