#!/usr/bin/env python3
"""
天气助手 Agent - 使用LiteLLM连接豆包模型
"""
import os
import sys
import pathlib
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

# 加载环境变量
load_dotenv()

# 获取MCP服务器路径（相对于项目根目录）
PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
mcp_server_path = str(PROJECT_ROOT / "mcp_server" / "weather_mcp_server.py")

# 创建MCP工具集
mcp_tools = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='python',
            args=[mcp_server_path],
        ),
    ),
)

# 使用LiteLLM连接豆包模型（OpenAI兼容API）
# 豆包通过自定义OpenAI兼容API访问
model = LiteLlm(
    model="openai/doubao-seed-1-8-251228",  # 使用openai/前缀指定OpenAI兼容服务
    api_base="http://172.24.140.24:3000/v1",
    api_key=os.getenv("LLM_API_KEY"),
)

# 根Agent - 必须命名为 root_agent，ADK Web会自动加载
root_agent = Agent(
    model=model,  # 使用LiteLlm包装的豆包模型
    name='weather_assistant',
    description='天气查询助手 - 使用豆包模型和MCP工具',
    instruction="""你是一个专业的天气助手。

你可以使用以下工具：
- get_weather: 获取特定城市的天气
- get_all_cities: 获取支持的城市列表  
- compare_weather: 比较两个城市的天气

请根据用户的要求使用这些工具，并提供有用的建议。支持的城市：北京(beijing)、上海(shanghai)、广州(guangzhou)。
""",
    tools=[mcp_tools],
)
