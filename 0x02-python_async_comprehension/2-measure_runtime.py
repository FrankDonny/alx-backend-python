#!/usr/bin/env python3
"""module two for async generators"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """function for asynccio.gather"""
    start = time.time()
    results = await asyncio.gather(*(async_comprehension() for i in range(4)))
    totalTime = time.time() - start
    return totalTime
