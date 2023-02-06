#!/usr/bin/env python3
"""second async module"""
import asyncio
import random
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function for this module"""
    wait_nRetVal: List[float] = []
    for _ in range(n):
        retVal: float = await task_wait_random(max_delay)
        wait_nRetVal.append(retVal)
        wait_nRetVal = sorted(wait_nRetVal)
    return wait_nRetVal


async def task_wait_random(max_delay: int = 10) -> float:
    """async coroutine that returns a random float number"""
    delay: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
