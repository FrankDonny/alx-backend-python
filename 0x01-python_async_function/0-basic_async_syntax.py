#!/usr/bin/env python3
"""asunc module for task 0"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async coroutine that returns a random float number"""
    delay: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
