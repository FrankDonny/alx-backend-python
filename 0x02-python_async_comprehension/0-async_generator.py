#!/usr/bin/env python3
"""module one for async generators"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """method that runs 10x and asynchronously wait 1 second"""
    for _ in range(10):
        yield random.uniform(0, 10.0)
        await asyncio.sleep(1)
