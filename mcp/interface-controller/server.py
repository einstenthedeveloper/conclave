import json
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

import browser as br
import logger as lg

app = Server("interface-controller")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(name="browser_navigate", description="Navigate to a URL", inputSchema={
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "timeout": {"type": "integer", "default": 60000},
            },
            "required": ["url"],
        }),
        Tool(name="browser_click", description="Click an element (tries selectors in order)", inputSchema={
            "type": "object",
            "properties": {
                "selectors": {"type": "array", "items": {"type": "string"}},
                "timeout": {"type": "integer", "default": 8000},
            },
            "required": ["selectors"],
        }),
        Tool(name="browser_type", description="Type text into an element", inputSchema={
            "type": "object",
            "properties": {
                "selectors": {"type": "array", "items": {"type": "string"}},
                "text": {"type": "string"},
                "delay": {"type": "integer", "default": 40},
            },
            "required": ["selectors", "text"],
        }),
        Tool(name="browser_upload", description="Upload a file via file chooser", inputSchema={
            "type": "object",
            "properties": {
                "selectors": {"type": "array", "items": {"type": "string"}},
                "filepath": {"type": "string"},
            },
            "required": ["selectors", "filepath"],
        }),
        Tool(name="browser_screenshot", description="Take a screenshot of the current page", inputSchema={
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        }),
        Tool(name="browser_wait_for", description="Wait for an element to appear", inputSchema={
            "type": "object",
            "properties": {
                "selectors": {"type": "array", "items": {"type": "string"}},
                "timeout": {"type": "integer", "default": 10000},
            },
            "required": ["selectors"],
        }),
        Tool(name="browser_get_text", description="Get inner text of an element", inputSchema={
            "type": "object",
            "properties": {"selector": {"type": "string"}},
            "required": ["selector"],
        }),
        Tool(name="session_save", description="Save current browser session cookies", inputSchema={
            "type": "object",
            "properties": {"name": {"type": "string"}},
            "required": ["name"],
        }),
        Tool(name="session_load", description="Load a saved browser session", inputSchema={
            "type": "object",
            "properties": {"name": {"type": "string"}},
            "required": ["name"],
        }),
        Tool(name="log_write", description="Write an entry to execution_log.json", inputSchema={
            "type": "object",
            "properties": {
                "status": {"type": "string", "enum": ["success", "failure", "unknown"]},
                "platform": {"type": "string"},
                "result": {"type": "string"},
                "failure_reason": {"type": "string", "default": "none"},
                "entry_id": {"type": "string"},
            },
            "required": ["status", "platform", "result"],
        }),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        if name == "browser_navigate":
            result = br.browser_navigate(arguments["url"], arguments.get("timeout", 60000))
        elif name == "browser_click":
            result = br.browser_click(arguments["selectors"], arguments.get("timeout", 8000))
        elif name == "browser_type":
            result = br.browser_type(arguments["selectors"], arguments["text"], arguments.get("delay", 40))
        elif name == "browser_upload":
            result = br.browser_upload(arguments["selectors"], arguments["filepath"])
        elif name == "browser_screenshot":
            result = br.browser_screenshot(arguments["path"])
        elif name == "browser_wait_for":
            result = br.browser_wait_for(arguments["selectors"], arguments.get("timeout", 10000))
        elif name == "browser_get_text":
            result = br.browser_get_text(arguments["selector"])
        elif name == "session_save":
            result = br.session_save(arguments["name"])
        elif name == "session_load":
            result = br.session_load(arguments["name"])
        elif name == "log_write":
            result = lg.log_write(
                status=arguments["status"],
                platform=arguments["platform"],
                result=arguments["result"],
                failure_reason=arguments.get("failure_reason", "none"),
                entry_id=arguments.get("entry_id"),
            )
        else:
            result = {"ok": False, "error": f"unknown tool: {name}"}
    except Exception as e:
        result = {"ok": False, "error": str(e)}

    return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False))]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
