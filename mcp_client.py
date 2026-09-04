from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run_client(server_script: str):
    server_params = StdioServerParameters(
        command=".venv\\Scripts\\python.exe",
        args=[server_script],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            print("Available tools:")

            for tool in tools.tools:
                print(f"- {tool.name}")

            result = await session.call_tool(
                "add",
                arguments={"a": 10, "b": 20},
            )

            print("\nResult:")
            print(result)