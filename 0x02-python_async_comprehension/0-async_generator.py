#!/usr/bin/env python3
"""module one for async generators"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """method that runs 10x and asynchronously wait 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10.0)


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
