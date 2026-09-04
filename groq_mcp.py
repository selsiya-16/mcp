import asyncio
import os
import json

from dotenv import load_dotenv
from groq import Groq

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in .env")

groq = Groq(api_key=api_key)


async def main():
    server_params = StdioServerParameters(
        command=".venv\\Scripts\\python.exe",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            # Get MCP tools
            tools_result = await session.list_tools()

            print("Available MCP tools:")

            for tool in tools_result.tools:
                print(f"- {tool.name}")

            # Convert MCP tools to Groq tool format
            groq_tools = []

            for tool in tools_result.tools:
                groq_tools.append(
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description or "",
                            "parameters": tool.input_schema,
                        },
                    }
                )

            # Ask Groq
            messages = [
                {
                    "role": "user",
                    "content": "What is 10 + 20?",
                }
            ]

            response = groq.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages,
                tools=groq_tools,
                tool_choice="auto",
            )

            message = response.choices[0].message

            # Check whether Groq wants to call an MCP tool
            if message.tool_calls:

                for tool_call in message.tool_calls:

                    tool_name = tool_call.function.name

                    arguments = json.loads(
                        tool_call.function.arguments
                    )

                    print("\nGroq selected MCP tool:")
                    print(f"Tool: {tool_name}")
                    print(f"Arguments: {arguments}")

                    # Call the MCP tool
                    result = await session.call_tool(
                        tool_name,
                        arguments=arguments,
                    )

                    print("\nMCP tool result:")
                    print(result)

            else:
                print("\nGroq response:")
                print(message.content)


if __name__ == "__main__":
    asyncio.run(main())