What is MCP?
MCP (Model Context Protocol) is a standardized protocol used to connect AI applications with external tools, data, and services.
MCP Components                                                                                     
MCP Host    -  The AI application that provides the overall AI experience.                                     
MCP Client  -  The component inside the host that communicates with MCP servers.                                
MCP Server  -  Exposes tools, resources, and prompts to MCP clients.  
Tool	    -  An executable function that allows the AI to perform an action.
Resource	-  Data or context that can be provided to the AI.                                                                                |
MCP Architecture
An AI application can use an MCP server that provides a calculator tool.
How MCP Works
MCP and API
API   -  An API (Application Programming Interface) allows one software application or service to communicate with another software application or service.
MCP   -  MCP provides a standardized way for AI applications to discover and use external tools, data, and services.
MCP does not replace APIs. An MCP server can use APIs internally to communicate with external services.