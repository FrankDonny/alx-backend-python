#!/usr/bin/env python3
"""third async module"""
import asyncio
import time
from typing import Any

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start: Any = time.time()
    asyncio.run(wait_n(0, max_delay))
    total_time: Any = time.time() - start
    return total_time/n
