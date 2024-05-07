#!/usr/bin/env python3
"""Asynchronous programming with coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (float values)
    """
    results = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(results)
