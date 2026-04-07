#!/usr/bin/env python3
"""
天气信息MCP服务器示例
演示如何创建一个简单的MCP服务器来暴露天气查询功能
"""
import asyncio
import json
from mcp import types as mcp_types
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# 创建MCP服务器实例
app = Server("weather-mcp-server")

# 模拟天气数据
WEATHER_DATA = {
    "beijing": {
        "city": "北京",
        "temperature": 20,
        "condition": "晴天",
        "humidity": 45,
        "wind_speed": 10
    },
    "shanghai": {
        "city": "上海",
        "temperature": 22,
        "condition": "多云",
        "humidity": 60,
        "wind_speed": 12
    },
    "guangzhou": {
        "city": "广州",
        "temperature": 28,
        "condition": "雨",
        "humidity": 75,
        "wind_speed": 15
    }
}


@app.list_tools()
async def list_tools() -> list[mcp_types.Tool]:
    """
    MCP服务器的工具列表处理函数
    返回该服务器提供的所有工具定义
    """
    print("MCP Server: 客户端请求工具列表...")
    return [
        mcp_types.Tool(
            name="get_weather",
            description="获取指定城市的天气信息。支持的城市：beijing, shanghai, guangzhou",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称 (英文: beijing, shanghai, guangzhou)"
                    }
                },
                "required": ["city"]
            }
        ),
        mcp_types.Tool(
            name="get_all_cities",
            description="获取所有支持的城市列表",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        mcp_types.Tool(
            name="compare_weather",
            description="比较两个城市的天气信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "city1": {
                        "type": "string",
                        "description": "第一个城市名称"
                    },
                    "city2": {
                        "type": "string",
                        "description": "第二个城市名称"
                    }
                },
                "required": ["city1", "city2"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[mcp_types.Content]:
    """
    MCP服务器的工具执行处理函数
    接收客户端的工具调用请求，执行相应的功能
    """
    print(f"MCP Server: 执行工具 '{name}' with arguments: {arguments}")
    
    try:
        if name == "get_weather":
            city = arguments.get("city", "").lower()
            if city not in WEATHER_DATA:
                return [
                    mcp_types.TextContent(
                        type="text",
                        text=json.dumps({
                            "error": f"城市 '{city}' 不支持。支持的城市: {', '.join(WEATHER_DATA.keys())}"
                        }, ensure_ascii=False)
                    )
                ]
            
            weather_info = WEATHER_DATA[city]
            return [
                mcp_types.TextContent(
                    type="text",
                    text=json.dumps(weather_info, ensure_ascii=False, indent=2)
                )
            ]
            
        elif name == "get_all_cities":
            cities = list(WEATHER_DATA.keys())
            return [
                mcp_types.TextContent(
                    type="text",
                    text=json.dumps({
                        "cities": cities,
                        "count": len(cities)
                    }, ensure_ascii=False, indent=2)
                )
            ]
            
        elif name == "compare_weather":
            city1 = arguments.get("city1", "").lower()
            city2 = arguments.get("city2", "").lower()
            
            if city1 not in WEATHER_DATA or city2 not in WEATHER_DATA:
                return [
                    mcp_types.TextContent(
                        type="text",
                        text=json.dumps({
                            "error": "一个或两个城市不支持"
                        }, ensure_ascii=False)
                    )
                ]
            
            comparison = {
                "city1": WEATHER_DATA[city1],
                "city2": WEATHER_DATA[city2],
                "comparison": {
                    "temperature_diff": WEATHER_DATA[city1]["temperature"] - WEATHER_DATA[city2]["temperature"],
                    "warmer_city": city1 if WEATHER_DATA[city1]["temperature"] > WEATHER_DATA[city2]["temperature"] else city2
                }
            }
            return [
                mcp_types.TextContent(
                    type="text",
                    text=json.dumps(comparison, ensure_ascii=False, indent=2)
                )
            ]
        else:
            return [
                mcp_types.TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"工具 '{name}' 未知"
                    }, ensure_ascii=False)
                )
            ]
    except Exception as e:
        print(f"MCP Server: 执行工具时出错: {e}")
        return [
            mcp_types.TextContent(
                type="text",
                text=json.dumps({
                    "error": str(e)
                }, ensure_ascii=False)
            )
        ]


async def main():
    """
    MCP服务器主函数
    启动Stdio服务器，与客户端通信
    """
    print("启动天气MCP服务器...")
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP服务器: 与客户端进行握手...")
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=app.name,
                server_version="1.0.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        print("MCP服务器: 运行循环结束或客户端断开连接")


if __name__ == "__main__":
    print("天气 MCP 服务器示例")
    print("-" * 50)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nMCP服务器已被用户中断")
    except Exception as e:
        print(f"MCP服务器错误: {e}")
    finally:
        print("MCP服务器进程退出")
