# -*- coding: utf-8 -*-
"""Example for stateful MCP client."""
import asyncio
import os

from agentscope.agent import ReActAgent, UserAgent
from agentscope.mcp import HttpStatelessClient
from agentscope.tool import Toolkit

from agent_project import amap_api_key, create_model_and_formatter

# 切换 provider: "openai" 或 "dashscope"
PROVIDER = os.getenv("MODEL_PROVIDER", "openai")


async def main() -> None:
    """Create a stateful MCP client and use it to chat with the model."""

    # 创建高德 MCP client
    client = HttpStatelessClient(
        name="amap",
        transport="streamable_http",
        url=f"https://mcp.amap.com/mcp?key={amap_api_key}",
    )

    # 注册工具
    toolkit = Toolkit()
    await toolkit.register_mcp_client(client)

    # 根据 PROVIDER 创建对应的 model 和 formatter
    model, formatter = create_model_and_formatter(PROVIDER)

    # 创建智能体
    agent = ReActAgent(
        name="Friday",
        sys_prompt="You are a helpful assistant named Friday.",
        model=model,
        formatter=formatter,
        toolkit=toolkit,
    )

    # 创建用户输入的代理
    user = UserAgent(name="user")

    # 通过消息的显式传递构建对话逻辑
    msg = None
    while True:
        msg = await agent(msg)
        msg = await user(msg)
        if msg.get_text_content() == "exit":
            break


asyncio.run(main())

# Query:
# - 搜索阿里云谷园区附近的咖啡厅
