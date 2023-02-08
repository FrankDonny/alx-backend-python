#!/usr/bin/env python3
"""module two for async generators"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """using an async comprehension"""
    return [num async for num in async_generator()]


async def main():
    print(await async_comprehension())

asyncio.run(main())
