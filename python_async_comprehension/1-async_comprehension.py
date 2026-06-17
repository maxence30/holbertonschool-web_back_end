#!/usr/bin/env python3
"""Module contenant une coroutine utilisant une compréhension asynchrone."""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Collecte les valeurs produites par async_generator."""
    return [i async for i in async_generator()]
