#!/usr/bin/env python3
"""multiplier annotated module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returning a function"""
    return lambda num: num * multiplier
