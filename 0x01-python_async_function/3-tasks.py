#!/usr/bin/env python3
"""fourth async module"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """using a normal function to execute async"""
    task: Any = asyncio.create_task(wait_random(max_delay))
    return task
