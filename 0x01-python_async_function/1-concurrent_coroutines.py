#!/usr/bin/env python3
"""second async module"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function for this module"""
    wait_nRetVal: List[float] = []
    for _ in range(n):
        retVal: float = await wait_random(max_delay)
        wait_nRetVal.append(retVal)
        wait_nRetVal = sorted(wait_nRetVal)
    return wait_nRetVal
