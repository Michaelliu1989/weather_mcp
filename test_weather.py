#!/usr/bin/env python3
"""
测试脚本用于验证weather-x工具功能
"""

import asyncio
from weather import mcp, get_alerts

async def test_weather_tool():
    """测试天气工具功能"""
    print("Testing weather tool...")

    # 测试获取天气警报功能
    try:
        result = await get_alerts("北京")
        print("Weather alert result:")
        print(result)
    except Exception as e:
        print(f"Error getting weather alerts: {e}")

if __name__ == "__main__":
    asyncio.run(test_weather_tool())