#!/usr/bin/env python3
"""fourth async module"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    task: Any = asyncio.create_task(wait_random())
    return task
