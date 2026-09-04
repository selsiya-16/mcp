import asyncio

from mcp_client import run_client

if __name__ == "__main__":
    asyncio.run(run_client("server.py"))