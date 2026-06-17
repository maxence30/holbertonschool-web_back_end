#!/usr/bin/env python3
"""Module containing a coroutine that uses an async comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect ten random numbers generated asynchronously."""
    return [i async for i in async_generator()]
