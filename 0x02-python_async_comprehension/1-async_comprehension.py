#!/usr/bin/env python3
"""Async generator"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of random numbers using an async comprehension"""
    return [num async for num in async_generator()]
