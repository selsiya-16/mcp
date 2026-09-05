from mcp.server.mcpserver import MCPServer

from database import (
    create_database,
    add_customer,
    list_customers,
    get_customer,
    delete_customer
)

mcp = MCPServer("MCP Learning Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b

@mcp.tool()
def create_customer(
    name: str,
    email: str,
    phone: str = ""
) -> dict:
    """Create a new customer."""

    return add_customer(name, email, phone)

@mcp.tool()
def get_all_customers() -> list:
    """Get all customers."""

    return list_customers()

@mcp.tool()
def find_customer(customer_id: int) -> dict:
    """Find a customer by ID."""

    return get_customer(customer_id)

@mcp.tool()
def remove_customer(customer_id: int) -> str:
    """Delete a customer by ID."""

    return delete_customer(customer_id)

@mcp.resource("customers://all")
def customer_resource() -> str:
    """Provide all customers as a resource."""

    customers = list_customers()

    return str(customers)

if __name__ == "__main__":
    create_database()
    mcp.run()